# Rest Template 사용하기 - POST

- 이전 내용
    - 클라이언트가 서버로 요청을 보내서 응답을 받는 형태

- Rest Template을 통한 POST 방식 통신

## Client 설정

- dto/UserRequest.java
    ```java
    package com.example.client.dto;

    public class UserRequest {

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
            return "UserResquest{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    '}';
        }
    }
    ```

- RestTemplateService.java
    ```java
    @Service
    public class RestTemplateService {

        public UserResponse hello(){

            URI uri = UriComponentsBuilder
                    .fromUriString("http://localhost:9090")
                    .path("/api/server/hello")
                    .queryParam("name", "steve")
                    .queryParam("age", 100)
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

        // POST
        
        public UserResponse post(){
            // http://localhost:9090/api/server/user/{userId}/name/{userName} (user로 등록시키는 주소, userId, userName도 path variable로 넣어줌)
            // 실제로 이렇게 사용하지는 않음(예제 용도)

            // 주소 만들기
            URI uri = UriComponentsBuilder
                    .fromUriString("http://localhost:9090")
                    .path("/api/server/user/{userId}/name/{userName}")
                    .encode()   // encod() : URI safe하게 만듦
                    .build()
                    .expand(100, "steve") // expand() : 순서대로 path variable 변수와 매칭됨, ','로 구분!
                    .toUri();
            // 만들어진 URI 확인
            System.out.println(uri);

            // request body 만들기 (JSON으로 만드는 것이 아니라 object로 만들면 Object Mapper가 자연적으로 바꿔주는 과정 거침)
            // http body -> object -> object mapper -> json -> rest template -> http body json
            UserRequest req = new UserRequest();
            req.setName("steve");
            req.setAge(10);

            // rest template으로 request 보내기
            RestTemplate restTemplate = new RestTemplate();
            // 응답받을 타입 지정
            // 해당 주소(uri)에 request body(req)를 만들어서 특정 타입(UserResponse 타입)의 응답을 받음!
            ResponseEntity<UserResponse> response = restTemplate.postForEntity(uri, req, UserResponse.class);

            System.out.println(response.getStatusCode());
            System.out.println(response.getHeaders());
            System.out.println(response.getBody());

            return response.getBody();
        }
    }
    ```

- ApiController.java
```java
@RestController
@RequestMapping("/api/client")
public class ApiController {

    private final RestTemplateService restTemplateService;

    public ApiController(RestTemplateService restTemplateService) {
        this.restTemplateService = restTemplateService;
    }

    @GetMapping("/hello") // ??
    public UserResponse getHello(){
        // controller로 POST요청이 들어오면 RestTemplate을 통해서 server를 호출해서 응답을 받아서 response를 내림
        return restTemplateService.post();
    }
}
```

## Server 설정

- userId를 그냥 Age로 매칭시킴(단순 예제이므로..)
- controller/ServerApiController.java
    ```java
    @Slf4j
    @RestController
    @RequestMapping("/api/server")
    public class ServerApiController {

        @GetMapping("/hello")
        public User hello(@RequestParam String name, @RequestParam int age){
            User user = new User();
            user.setName(name);
            user.setAge(age);
            return user;
        }

        // POST 요청 받기

        // 일반적으로 주소에서 camel case를 쓰지는 않음!(예제이므로...)
        // 주소를 굳이 이렇게 적은 이유는 UriComponentBuilder에서 변화하는 부분(Path Variable)d에 대해서 작성하는 방법을 알아보기 위함임
        @PostMapping("/user/{userId}/name/{userName}")
        public User post(@RequestBody User user, @PathVariable int userId, @PathVariable String userName){
            log.info("userId : {}, userName : {}", userId, userName);
            log.info("client req : {}", user);

            return user;
        }
    }
    ```

## Talen API request

- http://localhost:8080/api/client/hello
- response body
    ```js
    {
    "name": "steve",
    "age": 10
    }
    ```
- client console output
    ```
    http://localhost:9090/api/server/user/100/name/steve
    200 OK
    [Content-Type:"application/json", Transfer-Encoding:"chunked", Date:"Wed, 08 Sep 2021 05:37:58 GMT", Keep-Alive:"timeout=60", Connection:"keep-alive"]
    UserResponse{name='steve', age=10}
    ```
- server console output
    ```
    2021-09-08 14:37:58.475  INFO 24328 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : userId : 100, userName : steve
    2021-09-08 14:37:58.478  INFO 24328 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : client req : User(name=steve, age=10)
    ```

### Header 관련

- Naver API, Kakao API 등에서는 Header 값을 지정하도록 되어있는데 우리는 Header 값을 지정하지 않고 오로지 Request Body만 채워서 보냈음


## 뭐로 내려줄지 모를 때 그냥 String 타입으로 받는 전략

- service/RestTemplateService.java
    - ResponseEntity<> 타입을 String으로 변경
    - postForEntity() 인자도 String.class으로 설정
    - 메서드 반환형을 void로 바꾸고 return 삭제
    ```java
    @Service
    public class RestTemplateService {

        public UserResponse hello(){
            URI uri = UriComponentsBuilder
                    .fromUriString("http://localhost:9090")
                    .path("/api/server/hello")
                    .queryParam("name", "steve")
                    .queryParam("age", 100)
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

        // POST
        public void post(){
    
            URI uri = UriComponentsBuilder
                    .fromUriString("http://localhost:9090")
                    .path("/api/server/user/{userId}/name/{userName}")
                    .encode()   
                    .build()
                    .expand(100, "steve")
                    .toUri();

            System.out.println(uri);

            UserRequest req = new UserRequest();
            req.setName("steve");
            req.setAge(10);

            // rest template으로 request 보내기
            RestTemplate restTemplate = new RestTemplate();
            // 응답받을 타입 지정
            // 해당 주소(uri)에 request body(req)를 만들어서 특정 타입의 응답을 받음!
            // ** 뭐로 내려줄지 모를 때 그냥 String 타입으로 받을 수 있음 **
            ResponseEntity<String> response = restTemplate.postForEntity(uri, req, String.class);

            System.out.println(response.getStatusCode());
            System.out.println(response.getHeaders());
            System.out.println(response.getBody());
        }
    }
    ```

- controller/ApiController.java
    - string으로 확인하기 위해 호출을 바꿈
        - 우선 post() 메서드를 호출하고
        - 빈 UserResponse 객체 하나 생성해서 response로 리턴함
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
            // controller로 POST요청이 들어오면 RestTemplate을 통해서 server를 호출해서 응답을 받아서 response를 내림

            // string으로 확인하기 위해 호출을 바꿈
            // post()를 호출하고
            restTemplateService.post();
            // 빈 것 하나 생성함 (예제이므로 테스트용도)
            return new UserResponse();
        }
    }
    ```

- Client console output
    ```
    http://localhost:9090/api/server/user/100/name/steve
    200 OK
    [Content-Type:"application/json", Transfer-Encoding:"chunked", Date:"Wed, 08 Sep 2021 05:47:27 GMT", Keep-Alive:"timeout=60", Connection:"keep-alive"]
    {"name":"steve","age":10} // string 문자열로 찍혔음!
    ```

➡ 이렇게 String으로 찍어보면서 어떤 값이 잘못 왔는지(ex, snake_case <-> camelCase)를 확인할 때 사용 가능  
➡ 굳이 이렇게 확인하지 않고 Talend API response 내용을 보고 맞추어도 됨  
➡ 대부분의 표준 API는 스펙 문서에 나와있는 대로 잘 맞추서 내려줌(걱정 노노)