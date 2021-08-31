# Exception

## Exception 처리

- Web Application 입장에서 에러가 났을 때 내려줄 수 있는 방법은 많지 않음
    1. 에러 페이지
    2. 4XX Error(클라이언트 오류) or 5XX Error(서버 오류)
    3. Client 200 외에 처리를 하지 못할 때는 200을 내려주고 Body에 result 코드나 별도의 에러 message 전달

- Web Application의 경우 이러한 에러를 한 곳에 모아서 처리하는 것이 가장 편함
    - try-catch를 통해 묶는 것보다는
    - **자연스럽게 throw를 시키거나 전체 Application에 대해서 한 번에 Exception을 처리**
        - 이러한 기능들을 Spring에서 제공함

- Exception 처리의 두 가지 방식

    |Annotation|설명|
    |--|--|
    |@ControllerAdvice|Global 예외 처리 및 특정 package/Controller 예외처리 [페이징 처리(화이트라벨 페이지, 에러 페이지를 내리는)하는 ViewResolver]|
    |@ExceptionHandler|특정 Controller의 예외처리, 특정 controller에 모든 에러가 catch되도록 적용 |

## Null Point Error 발생시키기 (GET)

- build.gradle에서 dependencies 추가
    ```java
    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-web'
        implementation 'org.springframework.boot:spring-boot-starter-validation'
        testImplementation 'org.springframework.boot:spring-boot-starter-test'
    }
    ```

- dto/User 클래스 생성
    ```java
    public class User {
        @NotEmpty
        @Size(min = 1, max = 10)
        private String name;

        @Min(1)
        @NotNull // null pointer가 들어올 수 없음
        private Integer age;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        @Override
        public String toString() {
            return "User{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    '}';
        }
    }
    ```

- controller/ApiController 생성
    ```java
    @RestController
    @RequestMapping("/api/user")
    public class ApiController {

        @GetMapping("")
        public User get(@RequestParam(required = false) String name, @RequestParam(required = false) Integer age){
            User user = new User();
            user.setName(name);
            user.setAge(age);

            // 에러 발생시키기 (required = false) : 값 넣어주지 않아도 error 발생 X
            // 우리가 age 값을 넣어주지 않으면 null pointer error 발생
            int a = 10 + age;

            return user;
        }
        @PostMapping("")
        public User post(@Valid @RequestBody User user){
            System.out.println(user);

            return user;

        }

    }
    ```

- Talend API에서 값 없이 GET 메서드 요청
    - http://localhost:8080/api/user?name&age

- 에러 발생
    - Response : 500 errror
        ```js
        {
        "timestamp": "2021-08-31T02:12:55.176+00:00",
        "status": 500,
        "error": "Internal Server Error",
        "path": "/api/user"
        }
        ```

    - console
        ```shell
        java.lang.NullPointerException: null
        at com.example.exception.controller.ApiController.get(ApiController.java:16) ~[main/:na]
        # .. 생략 ..
        ```

- 에러 발생 지점
    - controller/ApiController.java
        ```java
        @GetMapping("")
        public User get(@RequestParam(required = false) String name, @RequestParam(required = false) Integer age){
            User user = new User();
            user.setName(name);
            user.setAge(age);

            // 에러 발생시키기 (required = false) : 값 넣어주지 않아도 error 발생 X
            // 우리가 age 값을 넣어주지 않으면 null pointer error 발생
            int a = 10 + age;

            return user;
        }
        ```

    - dto/User.java
        ```java
        public void setAge(int age) {
            this.age = age;
        }
        ```
    
    - setAge()에서는 `int age`를 받아야 하지만 바깥의 get()에서는 `Integer age`를 받고 있음
        - Integer age가 setAge()에 들어가는 순간 null pointer error가 터짐

    - 기본적으로 Spring에서는 자체적으로 예외처리를 해줌

## POST 에러 처리

- server에는 에러의 원인이 무엇인지 메시지를 전송하지만 client 입장에서는 400 에러 밖에 나타나지 않음(불친절)

    - Talend API POST 메서드 요청
        ```js
        {
        "name" : "",
        "age" : 0
        }
        ```

    - 에러 발생(`에러 1`)
        - console
            ```shell
            Validation failed for argument [0] in public com.example.exception.dto.User com.example.exception.controller.ApiController.post(com.example.exception.dto.User) with 3 errors: [Field error in object 'user' on field 'name': rejected value []; codes [Size.user.name,Size.name,Size.java.lang.String,Size]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; arguments []; default message [name],10,1]; default message [크기가 1에서 10 사이여야 합니다]] [Field error in object 'user' on field 'age': rejected value [0]; codes [Min.user.age,Min.age,Min.int,Min]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.age,age]; arguments []; default message [age],1]; default message [1 이상이어야 합니다]] [Field error in object 'user' on field 'name': rejected value []; codes [NotEmpty.user.name,NotEmpty.name,NotEmpty.java.lang.String,NotEmpty]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; arguments []; default message [name]]; default message [비어 있을 수 없습니다]] 
            ```
        
        - Response Body(Client) : 400 error
            ```js
            {
            "timestamp": "2021-08-31T02:26:54.058+00:00",
            "status": 400,
            "error": "Bad Request",
            "path": "/api/user"
            }
            ```

1. ControllerAdvice를 통해 설정
    - advice 패키지에 GlobalControllerAdvice 클래스 추가
    - advice/GlobalControllerAdvice.java
        ```java
        // 이곳에서 전체적인 Exception을 전부 잡을 예정
        // RestController를 사용하는 경우 -> @RestControllerAdvice 사용
        // ViewResolver를 사용하는 경우 -> @ControllerAdvice 사용
        @RestControllerAdvice
        public class GlobalControllerAdvice {

            // 내가 잡고자 하는 메서드 생성
            // ResponseEntity 리턴 -> RestAPI이기 때문!
            // @ExceptionHandler(value = Exception.class) : 어떠한 예외를 잡을 것인가? value로 지정 (전체 Exception 모두 잡겠다)
            @ExceptionHandler(value = Exception.class)
            public ResponseEntity exception(Exception e){
                // Exception e : 위에서 설정한 예외를 매개변수로 받아서 사용
                System.out.println("---------------------");
                System.out.println(e.getLocalizedMessage());
                System.out.println("---------------------");
                
                // 서버에서 일어나는 예외는 Internal Server Error
                // 예외가 터지면 전부 이쪽에서 받음
                return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
            }
            
        }
        ```

    - 위와 동일한 Request를 보낸 결과 발생한 에러(`에러 2`)
        - console
            ```shell
            ---------------------
            Validation failed for argument [0] in public com.example.exception.dto.User com.example.exception.controller.ApiController.post(com.example.exception.dto.User) with 3 errors: [Field error in object 'user' on field 'name': rejected value []; codes [Size.user.name,Size.name,Size.java.lang.String,Size]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; arguments []; default message [name],10,1]; default message [크기가 1에서 10 사이여야 합니다]] [Field error in object 'user' on field 'age': rejected value [0]; codes [Min.user.age,Min.age,Min.int,Min]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.age,age]; arguments []; default message [age],1]; default message [1 이상이어야 합니다]] [Field error in object 'user' on field 'name': rejected value []; codes [NotEmpty.user.name,NotEmpty.name,NotEmpty.java.lang.String,NotEmpty]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; arguments []; default message [name]]; default message [비어 있을 수 없습니다]] 
            ---------------------
            ```
        - Response Body(Client) : 500 error
            ```
            No Content
            ```

    - 즉, 위 에러(`에러 1`)는 Spring boot에서 기본적으로 지정된 GlobalExceptionHandler가 동작해서 보내준 메시지
    - 아래 에러(`에러 2`)는  직접 Advice를 만들어서 등록한 것
        - 내가 지정한 ExceptionHandler를 통해 메시지가 찍힌 것


## 내가 원하는 Exception만 잡아보기

- ControllerAdivce에 클래스 이름 확인하는 코드 추가
    ```java
    @RestControllerAdvice
    public class GlobalControllerAdvice {

        @ExceptionHandler(value = Exception.class)
        public ResponseEntity exception(Exception e){
            
            // 클래스의 이름만 출력해보기 - 해당 클래스가 어디에 잘못된 예외인지 출력됨
            System.out.println(e.getClass().getName());

            System.out.println("---------------------");
            System.out.println(e.getLocalizedMessage());
            System.out.println("---------------------");
    
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
        }
        
    }
    ```

- console 결과
    ```shell
    org.springframework.web.bind.MethodArgumentNotValidException
    ---------------------
    Validation failed for argument [0] in public com.example.exception.dto.User com.example.exception.controller...
    ---------------------
    ```
    ➡ `MethodArgumentNotValidException` : 문제의 클래스는 이것이었음!

- 도출된 예외 결과만 따로 잡아서 처리하기
    - @ExceptionHandler의 value값에 처리하기 원하는 클래스 입력
    ```java
    @RestControllerAdvice
    public class GlobalControllerAdvice {

        // 전체 예외 잡는 부분
        @ExceptionHandler(value = Exception.class)
        public ResponseEntity exception(Exception e){
            
            // 클래스의 이름만 출력해보기 - 해당 클래스가 어디에 잘못된 예외인지 출력됨
            System.out.println(e.getClass().getName());

            System.out.println("---------------------");
            System.out.println(e.getLocalizedMessage());
            System.out.println("---------------------");
    
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("");
        }
    
        // ** 내가 원하는 부분만 따로 잡아서 처리하는 부분 **
        @ExceptionHandler(value = MethodArgumentNotValidException.class)
        public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
            // body에 메시지 담아서 리턴
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }

    }
    ```

    - ❗**전체 예외 처리하는 logic을 타지 않음**❗
    - ❗**console에는 더 이상 아무런 메시지도 출력되지 않음**❗

    - Response Body(Client) : 400 error
        ```
        Validation failed for argument [0] in public com.example.exception.dto.User com.example.exception.controller.ApiController.post(com.example.exception.dto.User) with 3 errors: [Field error in object 'user' on field 'name': rejected value []; codes [NotEmpty.user.name,NotEmpty.name,NotEmpty.java.lang.String,NotEmpty]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; arguments []; default message [name]]; default message [비어 있을 수 없습니다]] [Field error in object 'user' on field 'name': rejected value []; codes [Size.user.name,Size.name,Size.java.lang.String,Size]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.name,name]; arguments []; default message [name],10,1]; default message [크기가 1에서 10 사이여야 합니다]] [Field error in object 'user' on field 'age': rejected value [0]; codes [Min.user.age,Min.age,Min.int,Min]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [user.age,age]; arguments []; default message [age],1]; default message [1 이상이어야 합니다]] 
        ```

- 이렇게 직접 **글로벌**하게 예외를 잡아서 처리할 수 있음!
    - 예를들어 여러 개의 Controller(ApiController, UserApiController 등)가 존재한다고 하더라도 `GlobalControllerAdvice`는 특정한 클래스가 아니라 global하게 예외를 처리함

- basePackages 속성 (패키지 단위 예외처리)
    - `@RestControllerAdvice(basePackages = "com.example.execption.controller")`
    - '해당 패키지 하위에 있는 예외를 다 잡을거야' 의미

- 특정한 클래스만 지정해서 예외처리
    - 코드를 일관되게 하는 것이 아님
    - 해당 ApiController 내부에 @ExceptionHanlder 코드 직접 작성
        - 해당 Controller 안에서 일어나는 것만 관여하게 됨!
    ```java
    @RestController
    @RequestMapping("/api/user")
    public class ApiController {

        @GetMapping("")
        public User get(@RequestParam(required = false) String name, @RequestParam(required = false) Integer age){
            User user = new User();
            user.setName(name);
            user.setAge(age);

            // 에러 발생시키기 (required = false) : 값 넣어주지 않아도 error 발생 X
            // 우리가 age 값을 넣어주지 않으면 null pointer error 발생
            int a = 10 + age;

            return user;
        }
        @PostMapping("")
        public User post(@Valid @RequestBody User user){
            System.out.println(user);

            return user;

        }

        // 예외처리 메서드 직접 추가

        @ExceptionHandler(value = MethodArgumentNotValidException.class)
        public ResponseEntity methodArgumentNotValidException(MethodArgumentNotValidException e){
            // body에 메시지 담아서 리턴
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        }
    }
    ```

    - 🌟만약 `GlobalControllerAdvice` 안에도 해당 예외처리 코드가 있고 `ApiController` 안에도 예외처리 코드가 있다면 POST메서드의 에러가 발생했을 때 어떤 것이 작동할까?🌟
        - GlobalControllerAdvice에 예외 처리 코드가 들어가 있더라도 우선순위는 Controller에 직접 지정한 ExceptionHandler가 먼저 실행됨
        - 자연스럽게 해당 Controller의 ExceptionHandler가 맵핑이 되면 GlobalControllerAdvice의 ExceptionHandler는 동작을 하지 않음

## 정리

- **특정 Controller에 대해서 예외처리**를 하고 싶으면 해당 Controller 내에 직접 ExceptionHandler를 만들어주면됨 (특정 API에 작성하는 방식)
- **전체 시스템에 대해서 예외처리**를 하고 싶으면 @RestControllerAdvice 또는 @ControllerAdvice를 사용해서 ExceptionHandler를 지정해주면 됨 (전역으로 처리하는 방식)
    - RestController를 사용하는 경우 -> @RestControllerAdvice 사용
    - ViewResolver를 사용하는 경우 -> @ControllerAdvice 사용