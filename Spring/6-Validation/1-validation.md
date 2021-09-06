# Validation

## Validation

- 프로그래밍에 있어서 가장 필요한 부분
- 특히 Java에서는 null값에 대해서 접근하려고 할 때 null pointer exception이 발생함
- 이러한 부분을 방지하기 위해서 미리 검증을 하는 과정이 Validation
- 단순 예시
    - 매개변수가 3개밖에 안 되어서 if문으로 간단하게 처리 가능 
    ```java
    public void run(String account, Spring pw, int age){
        if(account == null || pw == null){
            return
        }

        if (age == 0){
            return 
        }
        // 정상 logic
    }
    ```

- 특정한 클래스 객체가 들어오거나 매개변수가 많아지면 if문이 복잡해짐
    - 검증 코드가 길어지기 때문에 business logic에서 벗어난 코드가 해당 부분에 작성될 수 있음
    - 검증 코드를 잘못 작성하게 되면 전체적인 서비스에 영향

- if문 validation 단점
    1. 검증해야 할 값이 많은 경우 코드의 길이가 길어짐
    2. 구현에 따라서 달라질 수 있지만 Service Logic과의 분리가 필요
    3. 흩어져 있는 경우 어디에서 검증을 하는지 알기 어려우며 재사용의 한계가 있음
    4. 구현에 따라 달라질 수 있지만 검증 Logic이 변경되는 경우 테스트 코드 등 참조하는 클래스에서 Logic이 변경되어야 하는 부분이 발생할 수 있음
    
- Validation은 변화가 생겨서는 안 되고(=일관적이여야 함) 한 번 작성되고 나면 거기에 business logic이 들어가선 안 됨!

- 이러한 Validation을 잘 처리하기 위해 Spring에서는 일관된 validation이 존재하고 annotation으로 제공함
    - annotation을 변수에 붙여서 사용

    |annotation|의미|비고|
    |--|--|--|
    |@Size|문자 길이 측정|Int Type 불가|
    |@NotNull|null 불가||
    |@NotEmpty|null, "" 불가||
    |@NotBlank|null, "", " " 불가 ||
    |@Past|과거 날짜||
    |@PastOrPresent|오늘이거나 과거 날짜||
    |@Future|미래 날짜||
    |@FutureOrPresent|오늘이거나 미래 날짜||
    |@Pattern|정규식 적용||
    |@Max|최대값||
    |@Min|최소값||
    |@AssertTrue/False|별도 Logic 적용||
    |@Valid|해당 object validation 실행||

- Validation 세팅
    1. gradle dependencies 추가
        - `implementation("org.springframework.boot:spring-boot-starter-validation")`
    2. bean validation spec 확인
        - bean validation에 대한 정의
            - 어떠한 annotation이 제공되고 있으며 어느 것을 활용하면 되는지 sample 확인 가능!
        - https://beanvalidation.org/2.0-jsr380/
    3. 핸드폰 번호 정규식 (테스트에 사용)
        - `"^\\d{2,3}-\\d{3,4}-\\d{4}$"`

## 어떠한 요청에 대한 request 값을 validation하기

- Controller 생성
    - validation 하기 위해서는 어떠한 값이 들어오는지 확인 가능해야 함
        - POST 사용
    - 어떤 데이터를 받을지 dto에서 정의(User)
        - @RequestBody로 User 정보 받아옴
    - 일종의 에코 프로그램
        - 입력으로 들어온 요청을 그대로 리턴
    - controller/ApiController.java
    ```java
    @RestController
    @RequestMapping("/api")
    public class ApiController {
        // validation 하기 위해서는 어떠한 값이 들어오는지 확인 가능해야 함 -> POST 사용
        @PostMapping("/user")
        public User user(@RequestBody User user) {
            // 여기서 어떤 데이터를 받을지 dto에서 정의(User)
            // request Body로 User 정보 받음
            System.out.println(user);
            return user;
        }
    }
    ```

- dto 생성
    - dto/User.java
    ```java
    public class User {

        private String name;
        private int age;
        private String email;
        private String phoneNumber;

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

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getPhoneNumber() {
            return phoneNumber;
        }

        public void setPhoneNumber(String phoneNumber) {
            this.phoneNumber = phoneNumber;
        }

        @Override
        public String toString() {
            return "User{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    ", email='" + email + '\'' +
                    ", phoneNumber='" + phoneNumber + '\'' +
                    '}';
        }
    }
    ```

- Talend에서 POST request 보내기

    - JSON request body
        - 이것은 잘못된 request임
        - client가 server에 정상적인 데이터를 보내지 않은 것
        ```js
        {
        "name" :  "홍길동",
        "age" : 10,
        "email" : "abcdefg",
        "phoneNumber" : "01011112222"
        }
        ```

    - console 출력 결과  
        `User{name='홍길동', age=10, email='abcdefg', phoneNumber='01011112222'}`
        - 하지만 이는 우리가 원하는 출력 형식이 아님 (email, phoneNumber)  
    
    

- 옛날식 코드
    - return 타입이 User가 아니라 ResponseEntity가 되어야 함
    - controller/ApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {
            @PostMapping("/user")
            public ResponseEntity user(@RequestBody User user) {
                System.out.println(user);

                // 옛날식 코드
                // return 타입이 User가 아니라 ResponseEntity가 되어야 함
                //if(user.getPhoneNumber() != "xxx-xxxx-xxxx"){ 또는
                if(user.getAge() >= 90){
                    return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(user);
                }

                return ResponseEntity.ok(user);
            }
        ```
    - 이 경우 request 정보에 age = 100으로 전송했다면
        - JSON request body
            ```js
            {
            "name": "홍길동",
            "age": 100,
            "email": "abcdefg",
            "phoneNumber": "01011112222"
            }
            ```
        - **Response 400 error 발생**

    - 지금은 validation이 age 하나지만 받아야할 값이 많아질수록 validation 코드가 길어지고 복잡해짐
        - 이런 것들을 잘 binding할 수 있도록 해주는 것이 바로 **Spring Validation**

- Spring Validation 사용
    - dto 클래스에 annotation 적용
        - @Email : 이메일에 대한 유효성 검사
        - dto/User.java
            ```java
            public class User {

                private String name;
                private int age;
                @Email
                private String email;
                private String phoneNumber;

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

                public String getEmail() {
                    return email;
                }

                public void setEmail(String email) {
                    this.email = email;
                }

                public String getPhoneNumber() {
                    return phoneNumber;
                }

                public void setPhoneNumber(String phoneNumber) {
                    this.phoneNumber = phoneNumber;
                }

                @Override
                public String toString() {
                    return "User{" +
                            "name='" + name + '\'' +
                            ", age=" + age +
                            ", email='" + email + '\'' +
                            ", phoneNumber='" + phoneNumber + '\'' +
                            '}';
                }
            }
            ```

    - Controller에서도 입력 받는 객체에 대해서 validation이 필요할 때 @Valid annotatino 적용
        - controller/ApiController.java
            ```java
            @RestController
            @RequestMapping("/api")
            public class ApiController {
                // 해당 객체에 대해서 validation이 필요할 때 @Valid annotation 달아야 함!
                @PostMapping("/user")
                public ResponseEntity user(@Valid @RequestBody User user) {
                    System.out.println(user);

                    return ResponseEntity.ok(user);
                }
            }
            ```

    - 잘못된 email 형식 보내기
        - JSON request body
        ```js
        {
        "name" :  "홍길동",
        "age" : 89,
        "email" : "abcdefg",
        "phoneNumber" : "01011112222"
        }
        ```
        - response 400 error(BAD REQUEST) 발생
        - console 결과  
            ` ...(생략)... default message [올바른 형식의 이메일 주소여야 합니다]] ]`

    - 정규식 사용하기
        - 사이트마다 입력 형식이 다를 수 있음
            - ex) 휴대폰 번호 '-' 없이 입력 또는 '-' 포함하여 입력
        - @Pattern(regexp = "") annotation 사용
        - 핸드폰 번호 정규식
            - `"^\\d{2,3}-\\d{3,4}-\\d{4}$"`
        - dto/User.java
            ```java
            public class User {

                private String name;
                private int age;
                @Email
                private String email;
                @Pattern(regexp = "^\\d{2,3}-\\d{3,4}-\\d{4}$")
                private String phoneNumber;

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

                public String getEmail() {
                    return email;
                }

                public void setEmail(String email) {
                    this.email = email;
                }

                public String getPhoneNumber() {
                    return phoneNumber;
                }

                public void setPhoneNumber(String phoneNumber) {
                    this.phoneNumber = phoneNumber;
                }

                @Override
                public String toString() {
                    return "User{" +
                            "name='" + name + '\'' +
                            ", age=" + age +
                            ", email='" + email + '\'' +
                            ", phoneNumber='" + phoneNumber + '\'' +
                            '}';
                }
            }
            ```
        - 형식에 맞춰서 보내야("010-1111-2222") 400 Bad Request error 발생하지 않음!

    - 정리
        - Spring valid annotation을 사용하면 if문 없이 간단하게 유효성 검사 가능
        - 발생한 에러 값을 가지고 따로 처리해줄 수도 있음 (예외처리는 뒤에서 배움)

- Spring Validation - BindingResult 사용하기
    - POST Method에서 BindingResult 객체도 함께 받음
    - **에러가 발생하는 것이 아니라 Validation에 대한 결과가 bindingResult 값으로 들어오게 됨!**
        - 그럼 bindingResult값을 확인해보자~
    - controller/ApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {
            // Validation에 대한 결과가 bindingResult 값으로 들어오게 함!
            @PostMapping("/user")
            public ResponseEntity user(@Valid @RequestBody User user, BindingResult bindingResult) {
                System.out.println(user);
                
                // bindingResult가 error값을 가지고 있는지 확인
                if (bindingResult.hasErrors()){
                    // binidngResult 메시지 만들기
                    StringBuilder sb = new StringBuilder();
                    bindingResult.getAllErrors().forEach(objectError -> {
                        // 어떠한 필드에서 에러가 났는지 확인
                        FieldError field = (FieldError) objectError;
                        // 디폴트 메시지 확인
                        String message = objectError.getDefaultMessage();

                        System.out.println("field : "+field.getField());
                        System.out.println(message);
                    });
                }
                return ResponseEntity.ok(user);
            }
            
        }
        ```

    - 유효하지 않은 request 전송
        - JSON request body
            ```js
            {
            "name" :  "홍길동",
            "age" : 89,
            "email" : "steve@gmail.com",
            "phoneNumber" : "01011112222"
            }
            ```
        - console 결과
            ```shell
            User{name='홍길동', age=89, email='steve@gmail.com',phoneNumber='01011112222'}
            field : phoneNumber
            "^\d{2,3}-\d{3,4}-\d{4}$"와 일치해야 합니다
            ```

    - 메세지 커스터마이징
        - @Pattern annotation의 message 속성 사용
        - dto/User.java
            ```java
            public class User {

                private String name;
                private int age;
                @Email
                private String email;
                @Pattern(regexp = "^\\d{2,3}-\\d{3,4}-\\d{4}$", message = "핸드폰 번호의 양식과 맞지 않습니다. 01x-xxx(x)-xxxx")
                private String phoneNumber;

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

                public String getEmail() {
                    return email;
                }

                public void setEmail(String email) {
                    this.email = email;
                }

                public String getPhoneNumber() {
                    return phoneNumber;
                }

                public void setPhoneNumber(String phoneNumber) {
                    this.phoneNumber = phoneNumber;
                }

                @Override
                public String toString() {
                    return "User{" +
                            "name='" + name + '\'' +
                            ", age=" + age +
                            ", email='" + email + '\'' +
                            ", phoneNumber='" + phoneNumber + '\'' +
                            '}';
                }
            }
            ```
        - Response 메시지에 담아주기
            - controller/ApiController.java
            ```java
            @RestController
            @RequestMapping("/api")
            public class ApiController {

                @PostMapping("/user")
                public ResponseEntity user(@Valid @RequestBody User user, BindingResult bindingResult) {
                    
                    System.out.println(user);

                    // bindingResult가 error값을 가지고 있는지 확인
                    if (bindingResult.hasErrors()){
                        // binidngResult 메시지 만들기
                        StringBuilder sb = new StringBuilder();
                        bindingResult.getAllErrors().forEach(objectError -> {
                            // 어떠한 필드에서 에러가 났는지 확인
                            FieldError field = (FieldError) objectError;
                            // 디폴트 메시지 확인
                            String message = objectError.getDefaultMessage();

                            System.out.println("field : "+field.getField());
                            System.out.println(message);

                            // 조금 더 보기좋게 응답 메시지로 만들기
                            sb.append("field : "+field.getField());
                            sb.append("messeage : "+message);

                        });
                        
                        // 에러 가지고 있기 때문에 마지막에 리턴시킴
                        // body에 메시지 string으로 넣어줌
                        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(sb.toString());
                    }

                    return ResponseEntity.ok(user);
                }
            }
            ```

        - 변경된 console 결과
            ```shell
            User{name='홍길동', age=89, email='steve@gmail.com', phoneNumber='01011112222'}
            field : phoneNumber
            핸드폰 번호의 양식과 맞지 않습니다. 01x-xxx(x)-xxxx
            ```

        - 변경된 response body 결과 (400 에러)
            - API를 사용하는 사람이 어느 부분에서 에러가 발생했는지 알 수 있음
            ```shell
            field : phoneNumbermesseage : 핸드폰 번호의 양식과 맞지 않습니다. 01x-xxx(x)-xxxx
            ```

    - BindingResult가 없다면 이후에 배우는 예외처리에서 같이 처리할 수 있음!

- Validation annotation 다양하게 적용하기

    - dto/User.java
        ```java
        public class User {

            @NotBlank
            private String name;
            @Max(value = 90)
            private int age;
            @Email
            private String email;
            @Pattern(regexp = "^\\d{2,3}-\\d{3,4}-\\d{4}$", message = "핸드폰 번호의 양식과 맞지 않습니다. 01x-xxx(x)-xxxx")
            private String phoneNumber;

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

            public String getEmail() {
                return email;
            }

            public void setEmail(String email) {
                this.email = email;
            }

            public String getPhoneNumber() {
                return phoneNumber;
            }

            public void setPhoneNumber(String phoneNumber) {
                this.phoneNumber = phoneNumber;
            }

            @Override
            public String toString() {
                return "User{" +
                        "name='" + name + '\'' +
                        ", age=" + age +
                        ", email='" + email + '\'' +
                        ", phoneNumber='" + phoneNumber + '\'' +
                        '}';
            }
        }
        ```

    - 모든 Validation annotation에는 각자의 default message 가지고 있음
        - ex) 나이 최대값을 넘어선 경우
            ```shell
            field : age
            90 이하여야 합니다
            ```
        - 원하는 형태로 바꿔서 사용할 수 있음!

    - Request 뿐만 아니라 우리가 만든 객체(User)에 대해서도 에러 확인하는 방법 존재
        - Custom Validation 활용하기!