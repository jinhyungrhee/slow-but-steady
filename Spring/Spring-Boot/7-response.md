# Response 내려주는 다양한 방법

- spring에서는 응답을 내려주는 방법은 여러 가지!

1. TEXT를 내려주는 방법

    - spring에서는 String의 형태로 response를 내림

    - 코드
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            @GetMapping("/text")
            public String text(@RequestParam String account) {
                return account;
            }
        }
        ```

2. JSON object를 내려주는 방법

    - JSON 디자인
        ```js
        {
            "name" : "steve",
            "age" : 10,
            "phoneNumber" : "010-1111-2222",
            "address" : "패스트캠퍼스"
        }
        ```

    - JSON default 자체가 UTF-8임!

    - dto 사용

    - 코드  
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {
        
            @PostMapping("/json")
            public User json(@RequestBody User user) {
                return user; // 응답이 user로 내려갈 땐 항상 200 Ok
            }
        }
        ```

    - User라는 객체를 RequestBody로 받아서 다시 user로 리턴하는 것
    
    - 실제 동작 
        - req -> object mapper -> object -> method -> object -> object mapper -> json -> response

    - response에서도 camelCase <-> snake_case 변환 두 가지 방법 (동일)
        1. `@JsonProperty` : 개별 변수에 적용
        2. `@JsonNaming` : 클래스 전체에 적용

3. 가장 명확하게 응답(Response)을 내려줄 수 있는 방법 : **ResponseEntity**
    
    - PUT의 경우 resource가 생성되면 201을 내려줌
        - 200 : resource 수정(UPDATE)
        - 201 : resource 생성(CREATED)

    - 201에 대한 응답을 내려주고 싶을 때는 (즉, Response 내려줄 때 HTTP Status를 지정해주고 싶을 때는) **ResponseEntity** 객체 사용 (\<generic type>)
        - 응답에 대한 커스터마이징이 필요할 때 ResponseEntity 사용
        - ResponseEntity를 통해 명확하게 값을 만들어서 응답을 내리는 것이 바람직!

    - 코드
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            @PutMapping("/put")
            public ResponseEntity<User> put(@RequestBody User user) {

                // 동일한 echo지만 CREATED라는 HTTP Method를 가지고 옴
                return ResponseEntity.status(HttpStatus.CREATED).body(user);
            }
        }
        ```

- spring에는 페이지(즉 HTML 파일)를 리턴하는 controller 존재!

    - `@RestController`처럼 API를 만드는 서버를 작성할 수도 있지만 `@Controller`처럼 실제로 페이지(HTML)를 리턴하는 서버도 작성할 수 있음!

    - `@Controller`
        - HTML 페이지 리소스를 찾음
        - 리턴 타입이 String이 되면 자동으로 resource에 있는 HTML 파일을 찾아가게 됨
        - PageController.java
            ```java
            @Controller
            public class PageController {

                @RequestMapping("/main")
                public String main() {
                    return "main.html";
                }
            }
            ```    
        
        
        -  이 부분에서 JSON을 어떻게 내려줄 것인가?
            1. @ResponseEntity 사용
            
            2. @ResponseBody 사용
                - 일반적으로 @Controller 사용 시 return type이 String이면 resource에서 HTML을 찾아서 리턴
                - 하지만 **@ResponseBody**를 붙이면 객체 자체를 리턴(return type이 특정한 객체)했을 때 Response Body를 만들어서 내림!
                - @Controller 사용하는 것이 그렇게 일반적이지 않기 때문에 정말 필요한 경우에만 사용
                    - 일반적으로는 ApiController를 만들어서 @RestController를 붙이고 거기에 대한 것들을 정의한 다음에 서비스하는 게 정확한 방법임!


- int, String은 Primitive Type

    - string이 default인 경우 null 값을 가짐
    - int가 default인 경우 0 값을 가짐
        - 만약 default값으로 null을 받고 싶다면 **int -> Integer** (Reference Type으로 변경)
        ```java
        public class User {
        
        // 생략

        // private int age;
        private Integer age;

        // 생략
        // object mapper는 get method를 확인함

        //public int getAge() {
        public Integer getAge() {
            return age;
        }
        ```

    - Response 결과
        - int(Primitive Type)
        ```js
        {
            "name": "steve",
            "age": 0,
            "phone_number": null,
            "address": "패스트 캠퍼스"
        }
        ```

        - Integer(Reference Type)
        ```js
        {
            "name": "steve",
            "age": null,
            "phone_number": null,
            "address": "패스트 캠퍼스"
        }
        ```
    

- 이러한 null 값들을 Response에 포함시키지 않고 싶을 때 
    - `@JsonInclude(JsonInclude.Include.NON_NULL)`
    - User 클래스에 붙여줌
    - JSON 규격서에도 명시 필요 (개발 편의를 위해)
    - response 결과
        ```js
        {
            "name": "steve",
            "address": "패스트 캠퍼스"
        }
        ```


- 코드 정리

    - ApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            // TEXT 내려주는 경우
            // GetMapping으로 넘어온 query parameter에 특정한 값을 return 시켜줌
            // spring에서 string의 형태로 response를 내림!
            @GetMapping("/text")
            public String text(@RequestParam String account) {
                return account;
            }

            // JSON 내려주는 경우
            // User라는 dto 사용
            // User라는 객체를 RequestBody로 받아서 user로 리턴한 것
            // 실제 동작 : req -> object mapper -> object -> method -> object -> object mapper -> json -> response
            @PostMapping("/json")
            public User json(@RequestBody User user) {
                return user; // 응답이 user로 내려갈 땐 항상 200 Ok
            }

            // PUT의 경우 resource가 생성되면 201을 내려줌 (PUT은 200[수정], 201[생성] 둘 다 사용)
            // 201에 대한 응답 내려주기
            // Response 내려줄 때 HTTP status 정해주기 -> ResponseEntity 객체 사용(<generic type>)
            // 응답에 대한 커스터마이징이 필요할 때 ResponseEntity 사용!
            // ResponseEntity를 통해 명확하게 값을 만들어서 내리는 것이 바람직함!
            @PutMapping("/put")
            public ResponseEntity<User> put(@RequestBody User user) {

                // 동일한 echo지만 CREATED라는 HTTP Method를 가지고 옴
                return ResponseEntity.status(HttpStatus.CREATED).body(user);
            }
        }
        ```
    
    - PageController.java
        ```java
        @Controller
        public class PageController {

            @RequestMapping("/main")
            public String main() {
                return "main.html";
            }

            // ResonseEntity

            @ResponseBody
            @GetMapping("/user")
            public User user() {
                // User user = new User(); // 구버전 객체 생성 방법
                var user = new User(); // Java 11 타입 추론 (단축 약어 var)
                user.setName("steve");
                user.setAddress("패스트 캠퍼스");
                return user;
            }
        }
        ```

    - dto/User.java
        ```java
        @JsonInclude(JsonInclude.Include.NON_NULL)
        @JsonNaming(value = PropertyNamingStrategy.SnakeCaseStrategy.class)
        public class User {
            // 리턴하고 싶은 데이터들 작성
            private String name;
            private Integer age;
            private String phoneNumber;
            private String address;

            public String getName() {
                return name;
            }

            public void setName(String name) {
                this.name = name;
            }

            public Integer getAge() {
                return age;
            }

            public void setAge(int age) {
                this.age = age;
            }

            public String getPhoneNumber() {
                return phoneNumber;
            }

            public void setPhoneNumber(String phoneNumber) {
                this.phoneNumber = phoneNumber;
            }

            public String getAddress() {
                return address;
            }

            public void setAddress(String address) {
                this.address = address;
            }

            //toString 메서드 오버라이딩

            @Override
            public String toString() {
                return "User{" +
                        "name='" + name + '\'' +
                        ", age=" + age +
                        ", phoneNumber='" + phoneNumber + '\'' +
                        ", address='" + address + '\'' +
                        '}';
            }
        }
        ```