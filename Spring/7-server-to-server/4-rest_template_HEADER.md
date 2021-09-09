# Rest Template 사용하기 - Header

- 보통은 Header에 Authorization key 같은 것들을 세팅함
- rest Template의 exchange()를 사용
    - 클래스 타입을 넣어서 호출하는 방법 / requestEntity를 넣어서 호출하는 방법

- 요청을 보낼 때는 requestEntity라는 것을 보냄

## Header 주고 받기

### Client

- requestEntity, exchange 사용해서 header를 실어서 보낼 수 있음
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

            RestTemplate restTemplate = new RestTemplate();
            ResponseEntity<String> response = restTemplate.postForEntity(uri, req, String.class);

            System.out.println(response.getStatusCode());
            System.out.println(response.getHeaders());
            System.out.println(response.getBody());

        }

        // client에서 header 보내기
        // requestEntity, exchange 사용
        public UserResponse exchange(){

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

            // requestEntity 생성
            // 요청을 보낼 때는 requestEntity라는 것을 보냄
            RequestEntity<UserRequest> requestEntity = RequestEntity
                    .post(uri) // request 주소
                    .contentType(MediaType.APPLICATION_JSON)
                    .header("x-authorization", "abcd") // request header 내용
                    .header("custom-header", "fffff") // header는 계속 추가해서 값을 넣어줄 수 있음
                    .body(req); // request body - 만들어놓은 req object 넣어줌

            RestTemplate restTemplate = new RestTemplate();
            // 호출하기
            // requestEntity를 보내고 UserResponse 받을 것임
            ResponseEntity <UserResponse> response = restTemplate.exchange(requestEntity, UserResponse.class);

            return response.getBody();
        }

    }
    ```

- RestApiControlle.java
    - exchange() 호출하기
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

            // header값도 보내기 위해 exchange()를 호출
            restTemplateService.exchange();
            // 빈 것 하나 생성함
            return new UserResponse();

        }
    }
    ```


### Server

- 요청받은 header 값 꺼내보기
- ServerApiController.java
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

        // server에서 Header 받기
        @PostMapping("/user/{userId}/name/{userName}")
        public User post(@RequestBody User user,
                        @PathVariable int userId,
                        @PathVariable String userName,
                        // 추가(이름 매칭)
                        @RequestHeader("x-authorization") String authorization,
                        @RequestHeader("custom-header") String customHeader
        ){
            log.info("userId : {}, userName : {}", userId, userName);
            // 추가한 Header 찍어보기
            log.info("authorization : {}, custom : {}", authorization, customHeader);
            log.info("client req : {}", user);

            return user;
        }
    }
    ```

### log 확인

- Talend API (GET)
    - http://localhost:8080/api/client/hello 

- server
    - authorization과 custom 값 잘 들어옴
    ```
    2021-09-09 11:40:22.394  INFO 27724 --- [nio-9090-exec-4] c.e.s.controller.ServerApiController     : userId : 100, userName : steve
    2021-09-09 11:40:22.395  INFO 27724 --- [nio-9090-exec-4] c.e.s.controller.ServerApiController     : authorization : abcd, custom : fffff
    2021-09-09 11:40:22.395  INFO 27724 --- [nio-9090-exec-4] c.e.s.controller.ServerApiController     : client req : User(name=steve, age=10)
    ```

- 중간 정리
    - server가 header를 요구한다면
        - client 쪽에서 **requestEntity**를 만들고 **Rest Template의 exchange()**를 호출하면 우리가 원하는 값을 header에 넣어서 보낼 수 있음!

## 다양한 형태로 존재하는 JSON

- body 안에 header가 들어있을 수도 있고, body 항목의 내용이 매번 바뀔 수도 있음
    - 이러한 형태가 default인 경우도 있음!
        ```js
        {
            "header": {
                
            },
            "body" : {
                
            }
        }
        ```
    - 예시1
        ```js
        {
            "header": {
                "response_code" : "OK"
            },
            "body" : {
                "name" : "steve",
                "age" : 10
            }
        }
        ```
    - 예시2
        ```js
        {
            "header": {
                "response_code" : "OK"
            },
            "body" : {
                "book" : "spring boot",
                "page" : 1024
            }
        }
        ```
        ➡ 이처럼 "header"와 "body"는 항상 고정되지만, "body"에 들어가는 내용이 달라지는 경우가 많이 있음  
        ➡ 이러한 경우 어떻게 디자인 해야 하는가?  
        ➡ **generic type**을 사용해서 디자인(❗굉장히 중요❗)

### Client
- 보낼 데이터 타입 만들기
    - client에서 dto/Req 생성
    - dto/Req.java
        ```java
        // generic Type을 받음으로써 body의 가변적인 부분 처리
        public class Req<T> {

            private Header header;

            // T(generic Type)를 어떻게 사용할 것인가?
            private T resBody;

            // header에 관련된 내용
            // header는 항상 같은 내용이 들어감
            public static class Header {
                private String responseCode;

                public String getResponseCode() {
                    return responseCode;
                }

                public void setResponseCode(String responseCode) {
                    this.responseCode = responseCode;
                }

                @Override
                public String toString() {
                    return "Header{" +
                            "responseCode='" + responseCode + '\'' +
                            '}';
                }
            }

            // body에 관련된 내용
            public Header getHeader() {
                return header;
            }

            public void setHeader(Header header) {
                this.header = header;
            }

            public T getResBody() {
                return body;
            }

            public void setResBody(T body) {
                this.body = body;
            }

            @Override
            public String toString() {
                return "Req{" +
                        "header=" + header +
                        ", body=" + body +
                        '}';
            }
        }
        ```

- 요청 보내는 부분 구현(generic exchange)
    - RestTemplateService.java 수정
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

                RestTemplate restTemplate = new RestTemplate();
                ResponseEntity<String> response = restTemplate.postForEntity(uri, req, String.class);

                System.out.println(response.getStatusCode());
                System.out.println(response.getHeaders());
                System.out.println(response.getBody());
            }

            public UserResponse exchange(){

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

                RequestEntity<UserRequest> requestEntity = RequestEntity
                        .post(uri)
                        .contentType(MediaType.APPLICATION_JSON)
                        .header("x-authorization", "abcd")
                        .header("custom-header", "fffff")
                        .body(req);

                RestTemplate restTemplate = new RestTemplate();
                ResponseEntity <UserResponse> response = restTemplate.exchange(requestEntity, UserResponse.class);

                return response.getBody();
            }

            // generic exchange 만들기
            public Req<UserResponse> genericExchange(){

                URI uri = UriComponentsBuilder
                        .fromUriString("http://localhost:9090")
                        .path("/api/server/user/{userId}/name/{userName}")
                        .encode()
                        .build()
                        .expand(100, "steve")
                        .toUri();
                System.out.println(uri);

                // http body -> object -> object mapper -> json -> rest template -> http body json

                // body에 userRequest가 들어감
                UserRequest userRequest = new UserRequest();
                userRequest.setName("steve");
                userRequest.setAge(10);

                // header와 req 각각 필요
                // userRequest를 generic으로 지정
                // req에 대한 body의 내용은 UserRequest로 지정되었기 때문에 req.getBody()를 하면 UserRequest를 가져오게 됨!
                Req<UserRequest> req = new Req<>();
                req.setHeader(
                        new Req.Header()
                );
                req.setResBody(
                        userRequest
                );

                // requestEntity
                // Req가 감싸고 있는 UserRequest(Req<UserRequest>)가 RequsetEntity임
                RequestEntity<Req<UserRequest>> requestEntity = RequestEntity
                        .post(uri) // request 주소
                        .contentType(MediaType.APPLICATION_JSON)
                        .header("x-authorization", "abcd") // request header 내용
                        .header("custom-header", "fffff") // header는 계속 추가해서 값을 넣어줄 수 있음
                        .body(req); // request body - 만들어놓은 req object 넣어줌

                // reqeustEntity를 Rest Template으로 보내기
                RestTemplate restTemplate = new RestTemplate();
                // generic에는 .class를 붙일 수 없음! -> 이에 대응하기 위해 ParameterizeTypeReference 사용!
                // 이것이 명확한 표시
                ResponseEntity<Req<UserResponse>> response
                        = restTemplate.exchange(requestEntity, new ParameterizedTypeReference<Req<UserResponse>>(){});
                // 하지만 이미 ResponseEntity에 type을 'Req<UserResponse>'로 이미 지정해놓았기 때문에 ParameterizedTypeReference안의 내용 생략 가능

                // response.getBody() : responseEntity의 body를 가져옴
                return response.getBody();
            }

        }
        ```

- ApiController에서 genericExchange() 호출
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
        public Req<UserResponse> getHello(){

            // genericExchange()를 호출하고 리턴
            return restTemplateService.genericExchange();
        }
    }
    ```


### Server

- server에서도 받을 데이터 타입 지정
    - dto/Req.java
        - lombok 사용
        ```java
        @Data
        @AllArgsConstructor
        @NoArgsConstructor
        public class Req<T> {

            private Header header;
            // body는 계속 바뀌므로 T(generic Type) 사용
            private T body;

            @Data
            @AllArgsConstructor
            @NoArgsConstructor
            public static class Header {
                private String responseCode;

            }
        }
        ```

- 서버에서 받는 부분 구현
    - ServerApiController의 post() 부분 수정
    - ServerApiController.java
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

            @PostMapping("/user/{userId}/name/{userName}")
            public Req<User> post(@RequestBody Req<User> user,
                            @PathVariable int userId,
                            @PathVariable String userName,
                            @RequestHeader("x-authorization") String authorization,
                            @RequestHeader("custom-header") String customHeader
            ){
                log.info("userId : {}, userName : {}", userId, userName);
                log.info("authorization : {}, custom : {}", authorization, customHeader);
                log.info("client req : {}", user);

                // Response시 똑같이 맞춰서 보내줘야 함
                Req<User> response = new Req<>();
                // response 만들어서 Header에 빈 값 아무거나 넣어줌
                response.setHeader(
                        new Req.Header()
                );
                // body에는 사용자가 보내왔던 user를 꺼내서 바로 echo로 response 내려줌
                response.setBody(user.getBody());

                return response;
            }
        }
        ```

### log 확인

- Talend API (GET)
    - http://localhost:8080/api/client/hello
    - Response Body
        ```
        {
        "header":{
        "responseCode": null
        },
        "resBody": null
        }
        ```
    - server console ouptu
        ```
        2021-09-09 19:09:43.069  INFO 26432 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : userId : 100, userName : steve
        2021-09-09 19:09:43.078  INFO 26432 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : authorization : abcd, custom : fffff
        2021-09-09 19:09:43.079  INFO 26432 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : client req : Req(header=Req.Header(responseCode=null), body=null)
        ```
    - 형식은 제대로 출력되었지만 null 값이 출력됨 

### 디버깅

- 클라이언트에는 문제 없어 보임
- 서버에서 HttpEntity를 사용해서 확인해봄
    - ServerApiController.java
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

            @PostMapping("/user/{userId}/name/{userName}")
            public Req<User> post(
                            // 순수한 HttpEntity 출력 (for 디버깅)
                            HttpEntity<String> entity,
                            @RequestBody Req<User> user,
                            @PathVariable int userId,
                            @PathVariable String userName,
                            @RequestHeader("x-authorization") String authorization,
                            @RequestHeader("custom-header") String customHeader
            ){
                // 순수한 request HttpEntity 내용 찍어보기
                log.info("req : {}", entity.getBody());
                log.info("userId : {}, userName : {}", userId, userName);
                log.info("authorization : {}, custom : {}", authorization, customHeader);
                log.info("client req : {}", user);

                Req<User> response = new Req<>();
                response.setHeader(
                        new Req.Header()
                );

                response.setBody(user.getBody());

                return response;
            }
        }
        ```
    - 500 에러 발생
        - 서버 콘솔에 `HttpMessageNotReadableException : Required request body is missing` 메시지 출력

- user 관련 부분 주석 처리하고 다시 시도
    - ServerApiController.java
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

            @PostMapping("/user/{userId}/name/{userName}")
            public Req<User> post(
                            // 순수한 HttpEntity 출력 (for 디버깅)
                            HttpEntity<String> entity,
                            // 일단 user는 사용하지 않으므로 주석처리
                            //@RequestBody Req<User> user,
                            @PathVariable int userId,
                            @PathVariable String userName,
                            @RequestHeader("x-authorization") String authorization,
                            @RequestHeader("custom-header") String customHeader
            ){
                log.info("req : {}", entity.getBody());
                log.info("userId : {}, userName : {}", userId, userName);
                log.info("authorization : {}, custom : {}", authorization, customHeader);
                // user 주석처리
                //log.info("client req : {}", user);

                Req<User> response = new Req<>();
                response.setHeader(
                        new Req.Header()
                );
            
                // user.getBody() 대신 잠시 null로 바꿔줌
                //response.setBody(user.getBody());
                response.setBody(null);

                return response;
            }
        }
        ```
    
    - Talend API request 결과
        - server console output
            ```
            2021-09-09 19:21:39.073  INFO 13808 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : req : {"header":{"responseCode":null},"resBody":{"name":"steve","age":10}}
            2021-09-09 19:21:39.074  INFO 13808 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : userId : 100, userName : steve
            2021-09-09 19:21:39.074  INFO 13808 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : authorization : abcd, custom : fffff
            ```
        - client가 server로 보낸 순수한 HttpEntity  
            ```
            2021-09-09 19:21:39.073  INFO 13808 --- [nio-9090-exec-1] c.e.s.controller.ServerApiController     : req : {"header":{"responseCode":null},"resBody":{"name":"steve","age":10}}
            ```
            - 여기에는 req로 "header"와 "resBody"가 잘 들어와 있음!
            - 서버의 Req와 User 클래스를 확인해보았더니 Req의 Body가 resBody로 수정되어있지 않았다. 그래서 매칭이 되지 않았던 것!!
                - Req.java
                    ```java
                    @Data
                    @AllArgsConstructor
                    @NoArgsConstructor
                    public class Req<T> {

                        private Header header;
                        // 수정해야 할 부분!
                        private T body;

                        @Data
                        @AllArgsConstructor
                        @NoArgsConstructor
                        public static class Header {
                            private String responseCode;

                        }
                    }
                    ```
            
- Req.java 수정
    ```java
    @Data
    @AllArgsConstructor
    @NoArgsConstructor
    public class Req<T> {

        private Header header;
        // 수정된 부분!
        private T resBody;

        @Data
        @AllArgsConstructor
        @NoArgsConstructor
        public static class Header {
            private String responseCode;

        }
    }
    ```

- ServerApiController.java 수정
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

        @PostMapping("/user/{userId}/name/{userName}")
        public Req<User> post(
                        //HttpEntity<String> entity,
                        @RequestBody Req<User> user,
                        @PathVariable int userId,
                        @PathVariable String userName,
                        @RequestHeader("x-authorization") String authorization,
                        @RequestHeader("custom-header") String customHeader
        ){
            //log.info("req : {}", entity.getBody());
            log.info("userId : {}, userName : {}", userId, userName);
            log.info("authorization : {}, custom : {}", authorization, customHeader);
            log.info("client req : {}", user);

            Req<User> response = new Req<>();
            response.setHeader(
                    new Req.Header()
            );
            response.setResBody(user.getResBody());

            return response;
        }
    }
    ```

- Talend API Resopnse Body 결과
    - 이제 제대로 내려줌!
    ```
    {
        "header":{
            "responseCode": null
        },
        "resBody":{
            "name": "steve",
            "age": 10
        }
    }
    ```

- ❗**client가 나한테 뭘 보냈는지 모르겠는 경우, 순수하게 HttpEntity로 받아서 getBody()를 해보면 client가 뭘 보냈는지 찍어볼 수 있음**❗
    - filter를 사용해서 찍어보는 것도 가능!


### 다양한 형태로 존재하는 JSON(= generic type 사용하기) 정리

- generic type 사용은 결국 '재사용'을 위한 것
    - JSON이 이러한 형태로 고정되어 있고 "body"의 내용만 바뀌면 여기에 클래스만 계속 바꾸어서 끼면 됨!
        - JSON
        ```js
        {
            "header": {
                "response_code" : "OK"
            },
            "body" : {
                "book" : "spring boot",
                "page" : 1024
            }
        }
        ```
    - 만약 이러한 형태로 코드를 짜지 않는다면 이러한 클래스를 계속 만들어야 함!