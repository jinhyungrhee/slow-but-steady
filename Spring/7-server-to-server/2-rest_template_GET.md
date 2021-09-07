# Rest Template 사용하기

- server를 두 개 띄우기 때문에 헷갈림 주의

## Client와 Server 구현하기

### Client 설정하기

- client 이름의 프로젝트 생성
    - resource/application.properties에 port 8080 지정
        ```
        server.port=8080
        ```

- 요청을 받아줄 server controller 먼저 생성 (??)

    - controller/ApiController.java
        ```java
        @RestController
        @RequestMapping("/api/client")
        public class ApiController {

            //@Autowired
            //private RestTemplateService restTemplateService;
            // @Autowired 는 옛날 방식 => 요즘은 '생성자 주입 방식'으로 바뀜!(명시적으로 알아보기 편함)
            // (프로젝트 할때는 @Autowired쓰고 lombok을 사용하여 조금 더 간단하게 설정)
            // alt+Enter 치고 첫번째 것 클릭 : 자동으로 default 생성자 만들어주면서 final에 대해서 spring에서 자동으로 주입해줌
            private final RestTemplateService restTemplateService;

            public ApiController(RestTemplateService restTemplateService) {
                this.restTemplateService = restTemplateService;
            }

            // get방식 호출
            @GetMapping("/hello")
            public String getHello(){
                // controller로 GET요청이 들어오면 RestTemplate을 통해서 server를 호출해서 응답을 받아서 response를 내림
                return restTemplateService.hello();
            }
        }
        ```

- 서비스 생성
    - 주소를 만들 때는 `UriComponenetBuilder` 사용
        - .encode() : 만약 parameter가 붙는다면 안정적으로 url 인코딩을 해서 보내야하기 때문에 사용

    - client가 되어야 하기 때문에 `Rest Template` 사용 ⭐
        - RestTemplate에서는 HTTP Method(GET, POST, PUT, DELETE..) 모두 지원
            - `.getForEntity` - 반환형태 responseType을 지정해줘야함(여러 가지 정보 얻을 수 있음)
            - `.getForObject` - ResonseEntity로 받는 것이 아니라 우리가 지정한 Generic Type으로 받을 수 있음
            - getForObject/getForEntity가 실행되는 순간이 Client에서 Http로 서버로 붇는 순간임!

    - service/RestTemplateService.java
        ```java
        @Service
        public class RestTemplateService {

            // 이 서비스 안에서 요청을 할 것임
            // http://localhost/api/server/hello
            // response
            public String hello(){
                // client가 되어야 하기 때문에 Rest Template 사용
                // 주소(URI) 만들 땐 UriComponentsBuilder 사용
                URI uri = UriComponentsBuilder
                        .fromUriString("http://localhost:9090")
                        .path("/api/server/hello")
                        .encode()
                        .build()
                        .toUri();
                // 주소 잘 생성되었는지 확인
                System.out.println(uri.toString());

                // RestTemplate을 이용하여 통신 (원래는 Pool을 만들어 놓고 써야 함)
                RestTemplate restTemplate = new RestTemplate();
                // "Object 형태를 가지고 uri에 요청하고 문자열(String)으로 결과를 받음"
                String result = restTemplate.getForObject(uri, String.class);
                // => getForObject가 실행되는 순간이 Client에서 Http GET Mehthod로 서버로 붇는 순간임!

                return result;
            }
        }
        ```

### Server 설정하기

- server 이름의 프로젝트 생성
    - lombok 체크
    - New Window 클릭하여 새 창에 띄움
        - client 프로젝트, server 프로젝트 동시에 돌림 (왼-client,오-server)
    - resource/application.properties에 port 9090 지정
        ```
        server.port=9090
        ```

- server쪽에서는 Client로부터 들어오는 Controller 필요

    - controller/ServerApiController.java
        ```java
        @RestController
        @RequestMapping("/api/server")
        public class ServerApiController {

            @GetMapping("/hello")
            public String hello(){
                return "hello server";
            }
        }
        ```

### 호출하기

- client의 hello() 메서드 호출
    - client 8080의 api/client/hello를 호출하면 restTemplate의 hello로 들어가서 9090 포트의 api/server/hello 즉 server의 hello를 호출시킴
    - 그러면 response로 "hello server"를 받아서 리턴시킴
        - ApiContoller.java (client)
            ```java
            @RestController
            @RequestMapping("/api/client")
            public class ApiController {

                private final RestTemplateService restTemplateService;

                public ApiController(RestTemplateService restTemplateService) {
                    this.restTemplateService = restTemplateService;
                }
                @GetMapping("/hello")
                public String getHello(){
                    return restTemplateService.hello();
                }
            }
            ```
        - RestTemplateService.java (client)
            - client가 되어서 호출하는 것이기 때문에 `.getForObject()`사용
                - response로 받을 형태 지정
                - server에서 JSON이 아닌 String을 내려주고 있기 때문에 String으로 데이터를 받은 것임(String.class)
            ```java
            @Service
            public class RestTemplateService {

                // 이 서비스 안에서 요청을 할 것임 (server의 hello를 호출함)
                public String hello(){
                    URI uri = UriComponentsBuilder
                            .fromUriString("http://localhost:9090")
                            .path("/api/server/hello")
                            .encode()
                            .build()
                            .toUri();
                    System.out.println(uri.toString());

                    RestTemplate restTemplate = new RestTemplate();
                    String result = restTemplate.getForObject(uri, String.class);

                    return result;
                }
            }
            ```
        - ServerApiController.java
            ```java
            @RestController
            @RequestMapping("/api/server")
            public class ServerApiController {

                @GetMapping("/hello")
                public String hello(){
                    // response로 "hello server"를 받아서 리턴시킴
                    return "hello server";
                }
            }
            ```

- Talend API
    - GET request
        - http://localhost:8080/api/client/hello
    - Response 
        - status code : `200`
        - response body : `hello server`
    - client console output
        ```
        http://localhost:9090/api/server/hello
        ```
        - 이 주소를 복사해서 browser에 입력해도 동일한 결과 페이지 등장
            - 결국 browser를 통해서 server를 호출하는 것임

### getForObject와 getForEntity의 차이

- client가 되어서 호출하는 것이기 때문에 `.getForObject()`나 `.getForEntity()` 사용

- getForObject는 Object 형태를 가지고 uri에 요청(?)하고 response로 받을 형태 지정
    - server에서 JSON이 아닌 String을 내려주고 있기 때문에 String으로 데이터를 받은 것임(String.class)
    ```java
    @Service
    public class RestTemplateService {

        public String hello(){

            URI uri = UriComponentsBuilder
                    .fromUriString("http://localhost:9090")
                    .path("/api/server/hello")
                    .encode()
                    .build()
                    .toUri();
            
            System.out.println(uri.toString());

            RestTemplate restTemplate = new RestTemplate();
            String result = restTemplate.getForObject(uri, String.class);

            return result;
        }
    }
    ```

- getForEntity()는 ResponseEntity형태로 결과값 받아옴
    - ResponseEntity의 data type을 지정할 수 있음
    - 여러 가지 상세한 정보를 받아볼 수 있음
        - header
        - status code
        - response body
        ```java
        @Service
        public class RestTemplateService {

            public String hello(){

                URI uri = UriComponentsBuilder
                        .fromUriString("http://localhost:9090")
                        .path("/api/server/hello")
                        .encode()
                        .build()
                        .toUri();
                
                System.out.println(uri.toString());

                RestTemplate restTemplate = new RestTemplate();
                // 'ResponseEntity를 받을 건데 data type은 String으로 받을 것임'을 지정
                ResponseEntity<String> result = restTemplate.getForEntity(uri, String.class);
                System.out.println(result.getStatusCode());
                System.out.println(result.getBody());

                // return getBody()를 해야 우리가 원하는 정확한 Body의 내용을 볼 수 있음
                return result.getBody();
            }
        }
        ```

    - Talend API GET request
        - http://localhost:8080/api/client/hello
        - console
            ```
            http://localhost:9090/api/server/hello
            200 OK
            hello server
            ```
        - response body
            ```
            hello server
            ```

## JSON 형태로 주고 받기

- JSON 형태 정의
    - "서버가 이런식으로 데이터를 줄 것임"
    ```js
    {
        "name" : "steve",
        "age" : 10
    }
    ```

### Client 설정하기

- Class 정의
    - 위와 같은 형태의 데이터를 받을 준비를 해야함
    - 받는 쪽(Client)에서 response에 대한 정의를 할 것이기 때문에 client 프로젝트에서 dto 패키지 생성
    - dto/UserResponse.java
        ```java
        public class UserResponse {

            private String name;
            private int age;

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
                return "UserResponse{" +
                        "name='" + name + '\'' +
                        ", age=" + age +
                        '}';
            }
        }
        ```

- ResposneEntity type을 우리가 정의한 클래스(UserResponse)로 받을 것임
    - 이때 Body 안에는 UserResponse가 들어있으므로 return type을 UserResponse로 변경
    - Client 쪽에서는 JSON으로 받은 데이터를 parsing하기 위해 RestTemplate의 getForEntity를 사용해서 GET에 대한 method를 처리할 수 있음!
    - RestTemplateService.java
        ```java
        @Service
        public class RestTemplateService {

            // *Body 안에 UserResponse가 들어있으므로 return type을 UserResponse로 변경*
            public UserResponse hello(){

                URI uri = UriComponentsBuilder
                        .fromUriString("http://localhost:9090")
                        .path("/api/server/hello")
                        .encode()
                        .build()
                        .toUri();
                
                System.out.println(uri.toString());

                RestTemplate restTemplate = new RestTemplate();
                // 우리가 정의한 UserResponse로 받을 것임
                ResponseEntity<UserResponse> result = restTemplate.getForEntity(uri, UserResponse.class);

                System.out.println(result.getStatusCode());
                System.out.println(result.getBody());

                // return getBody()를 해야 우리가 원하는 정확한 Body의 내용을 볼 수 있음
                // *이때 Body 안에는 UserResponse가 들어있으므로 return type을 UserResponse로 변경*
                return result.getBody();
            }
        }
        ```

- ApiController의 gethello() 메서드의 return 타입도 UserResponse로 맞춰줌
    - ApiController.java
        ```java
        @RestController
        @RequestMapping("/api/client")
        public class ApiController {

            private final RestTemplateService restTemplateService;

            public ApiController(RestTemplateService restTemplateService) {
                this.restTemplateService = restTemplateService;
            }

            @GetMapping("/hello")
            public UserResponse getHello(){
                return restTemplateService.hello();
            }
        }
        ```

### Server 설정하기

- Server에서도 JSON에 맞춰서 데이터를 제공해야 함
- Server는 lombok을 쓰고 있기 때문에 좀 더 간단함

- Class 정의
    - UserResponse와 동일한 형태이기만 하면됨(이름 달라도 OK)
    - dto/User.java
        ```java
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public class User {
            private String name;
            private int age;
        }
        ```

- ServerApiController로 요청이 들어왔을 때 Response 내려주기
    - ServerApiController.java
        ```java
        @RestController
        @RequestMapping("/api/server")
        public class ServerApiController {

            @GetMapping("/hello")
            public User hello(){
                // 요청이 들어오면 user 생성
                User user = new User();
                user.setName("steve");
                user.setAge(10);
                // object 그대로 리턴 (Response 내려줌)
                return user;
            }
        }
        ```

### Talend API GET reqeust

- http://localhost:8080/api/client/hello

- response body
    ```js
    {
    "name": "steve",
    "age": 10
    }
    ```

## Query Parameter를 사용하여 client - server 주고 받기

### Client

- UriComponentsBuilder
    - path에 여러 가지 내용들을 넣어줄 수 있음
        - queryParam()을 통해 query를 던질 수 있음
        - RestTemplateService.java
            ```java
            @Service
            public class RestTemplateService {

                public UserResponse hello(){

                    URI uri = UriComponentsBuilder
                            .fromUriString("http://localhost:9090")
                            .path("/api/server/hello")
                            .queryParam("name", "steve")
                            .queryParam("age", 10)
                            .encode()
                            .build()
                            .toUri();
                    
                    System.out.println(uri.toString());

                    
                    RestTemplate restTemplate = new RestTemplate();
                    ResponseEntity<UserResponse> result = restTemplate.getForEntity(uri, UserResponse.class);

                    System.out.println(result.getStatusCode());
                    System.out.println(result.getBody());

                    return result.getBody();
                }
            }
            ```
    - 이런식으로 queryParam을 추가하여 GET request를 하면
        - http://localhost:8080/api/client/hello
        - response body
            ```js
            {
            "name": "steve",
            "age": 10
            }
            ```
        - console output
            ```
            http://localhost:9090/api/server/hello?name=steve&age=10
            200 OK
            UserResponse{name='steve', age=10}
            ```
        ➡ response 내용은 동일하지만 만들어진 주소(URI)는 달라짐!  
        ➡ `.queryParam()`을 사용하면 주소 뒤에 query parameter가 붙게 됨

    - 이처럼 GET 주소를 만들 때 Query Parameter가 들어가야 하는 경우에는 `.queryParam()` 사용하면 됨!!

### Server

- Server쪽에서는 `@RequestParam` 어노테이션 사용하여 받음
- ServerApiController.java
    ```java
    @RestController
    @RequestMapping("/api/server")
    public class ServerApiController {

        @GetMapping("/hello")
        public User hello(@RequestParam String name, @RequestParam int age){
            User user = new User();
            // echo로 동작
            user.setName(name);
            user.setAge(age);
            // object 그대로 리턴
            return user;
        }
    }
    ```


## 정리

1. GET API를 쓸 때 어떠한 server가 어떤 data를 주는지 알게 되면(data의 내용이 정해지면) JSON 표준 규격을 보고 Class를 작성함
2. 그런 다음에 RestTemplate을 통해서 GET(getForEntity/getForObject)이나 POST(postForEntity/postForObject)의 형태로 데이터를 주고받으면 됨
    - 이번 예제에서는 GET으로 주소만 호출하면 됨으로 전혀 문제가 되지 않음
    - 하지만 POST로 보낼 때는 **Request Body**를 실어서 보내야 함!