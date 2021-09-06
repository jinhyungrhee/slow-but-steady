# Filter

## Filter란?

- Web Application에서 관리되는 영역
- Spring Boot Framework에서 Client로부터 오는 요청/응답 즉, 최초/최종 단계의 위치에 존재하는 것
- 이를 통해 요청/응답의 정보를 변경 가능
- Spring에 의해서 데이터가 변환되기 전의 순수한 Client의 요청/응답 값 확인 가능

- **유일하게 ServletRequest, ServletResponse의 객체를 변환할 수 있는 곳**

- 주로 Spring Framework에서는 **request/response의 Logging** 용도로 활용하거나 **인증과 관련된 Logic**들을 해당 Filter에서 처리
    - `예시 1` back-office 또는 Admin이라는 곳에서, 이 곳에 대한 모든 요청 또는 어떤 사용자가 들어왔고 어떤 것을 요청했는지에 관한 기록을 찍을 때
        - AOP의 경우 이미 객체로 mapping이 되었기 때문에 순수한 내용은 아님
        - Filter는 가장 앞단에서 Client의 요청이 들어오자마자 해당 Request Body나 Response Body를 기록함
    - `예시 2` 보안의 용도로 사용
        - 사용자 요청이 들어왔을 때 뒷단의 Interceptor를 타기도 전에 아예 앞단에서 세션 여부 등을 확인하여 reject하거나 unauthorized error를 발생시킴

- Filter에서 이러한 선처리/후처리를 통해 Service Business Logic과 분리시켜줌
    - Filter에서 순수하게 Request Header, Request Body, Response에 대한 기록들을 남김!

- AOP, Filter, Interceptor를 모두 걸어두면 Filter → Intercepter → AOP 순으로 동작
    - life cycle은 filter부터 시작됨!

## Filter에서 Client가 보낸 순수한 Request Body를 어떻게 기록하는지 확인

### Lombok 사용하기

- Lombok 활용
    - JAVA에서 사용하는 라이브러리
    - getter&setter, 생성자, toString 오버라이딩 등을 직접 작성하지 않고 깔끔하게 해결
        - `@Getter, @Setter` -> 변수의 Get, Set메서드 만들어줌
        - `@Data` -> getter&setter, hashcode(), toString(), equals()까지 전부 다 생성하여 lombok에서 관리
        - `@NoArgsConstructor` -> 기본생성자 생성(User()만 생성)
        - `@AllArgsConstructor` -> 전체생성자(User(String, int))
            - 왼쪽 하단 `Structure 탭`에서 확인 가능
    - lombok을 사용하면 getter&setter 만들 필요 없이 변수만 선언하고 @Data, @NoArgsConstructor, @AllArgsConstructor annotation만 붙여주면 됨!
    - dto/User.java
        ```java
        // lombok 사용
        //@Getter
        //@Setter
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public class User {

            private String name;
            private int age;

        }
        ```

    - lombok을 사용하는 Controller에는 `@Slf4j` 붙임
        - @Slf4j : lombok 사용시 Controller에 붙이는 어노테이션
        - lombok을 사용하면 Sysout 대신 log 사용 
            - 중괄호({})를 사용하여 문자열 뒤에 등장하는 객체와 매칭시킴
        - controller/ApiController.java
        ```java
        @Slf4j
        @RestController
        @RequestMapping("/api/user")
        public class ApiController {

            @PostMapping("")
            public User user(@RequestBody User user){
                // lombok을 사용하면 Sysout 대신 log 사용 - {} 사용(문자열 뒤의 객체와 매칭)
                log.info("User : {} , {}", user, user);

                return user;
            }
        }

        ```

     - 프로젝트 시작 시 lombok 설정 깜빡한 경우
        - buld.gradle 파일 dependencies에 코드 두 줄 추가
            ```
            compileOnly 'org.projectlombok:lombok'
            annotationProcessor 'org.projectlombok:lombok'
            ```
        - 컴파일 시 annotaionProcesor가 같이 동작하게 됨
        - 컴파일할 때만 lombok 사용(compileOnly)
            - User 클래스에 lombok 어노테이션을 붙여놓으면 Java Complier가 compile할 때 같이 complie하면서 getter&setter가 만들어지는 형태
            - 컴파일 시 이미 클래스 파일 안에다가 생성자나 getter&setter가 다 만들어 놓기 때문에 프로그램이 직접 실행될 때는 필요가 없다.

### Filter 생성

- filter 패키지 - GlobalFilter 클래스 생성
- Filter 상속받아 사용(javax.servlet.Filter)
- doFilter() 메서드 오버라이딩
- @Component로 filter 등록하기
    - Spring에 의해서 Bean으로 관리되도록 함
- @Slf4j 등록
    - 로그를 남기기 위해 등록
- doFilter 메서드 재정의(Overriding)
    - 이곳으로 reques와 response가 매개변수로 들어옴
    - `chain.doFilter(request, response)`를 기준으로
        - chain.doFilter가 동작하기 이전은 전처리 구간
        - chain.doFilter가 동작하고 난 다음은 후처리 구간
- 우선 전처리 구간만 구현
    - filter/GlobalFilter.java
        ```java
        @Slf4j
        @Component
        public class GlobalFilter implements Filter {
            @Override
            public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
                
                // 전처리 구간

                // url 받기 (*형변환 필요*) - Filter단에서는 Request와 Response에 대해서 변경 시켜줄 수 있음
                // HttpServletRequest : 이미 ServletRequest를 상속받은 클래스, 구현은 이미 되어있기 때문에 인터페이스만 바꿈
                HttpServletRequest httpServletRequest = (HttpServletRequest)request;
                HttpServletResponse httpServletResponse = (HttpServletResponse)response;

                String url = httpServletRequest.getRequestURI();
                //body 꺼내보기 - Buffered Reader 사용
                BufferedReader br = httpServletRequest.getReader();
                //출력하기
                br.lines().forEach(line -> {
                log.info("url : {}, line : {}",url ,line);
                });

                // 전처리 구간
                chain.doFilter(httpServletRequest, httpServletResponse);
                // 후처리 구간
                
                // 후처리 구간
            }
        }
        ```
    - Talend API로 POST request 보내기
        - request body
            ```json
            {
            "name" : "steve",
            "age" : 10
            }
            ```

    - console 확인
        - 어떤 주소로 요청을 했으며 body에 무슨 내용이 담겨 있는지 log를 찍어볼 수 있음
            ```
            2021-09-04 11:07:29.298  INFO 13036 --- [nio-8080-exec-1] com.example.filter.filter.GlobalFilter   : url : /api/user, line : {
            2021-09-04 11:07:29.300  INFO 13036 --- [nio-8080-exec-1] com.example.filter.filter.GlobalFilter   : url : /api/user, line :   "name" : "steve",
            2021-09-04 11:07:29.300  INFO 13036 --- [nio-8080-exec-1] com.example.filter.filter.GlobalFilter   : url : /api/user, line :   "age" : 10
            2021-09-04 11:07:29.300  INFO 13036 --- [nio-8080-exec-1] com.example.filter.filter.GlobalFilter   : url : /api/user, line : }
            ```
        - 에러도 발생
            ```
            java.lang.IllegalStateException: getReader() has already been called for this request
            at org.apache.catalina.connector.Request.getInputStream(Request.java:1075) ~[tomcat-embed-core-9.0.52.jar:9.0.52]
            at org.apache.catalina.connector.RequestFacade.getInputStream(RequestFacade.java:365) ~[tomcat-embed-core-9.0.52.jar:9.0.52]
            ```
            - java input stream에서 br.read()를 하면 파일을 커서 단위로 읽게 되고 커서가 점점 끝으로 이동하게 됨
            - 우리는 위의 코드에서 forEach를 통해 line을 모두 읽어버렸음
            - 커서 자체가 line의 제일 끝으로 가버려서 이미 body를 모두 읽어버린 상태가 됨
            - 그 상태에서 Spring이 Body에 있는 내용을 가지고 ApiController의 User라는 객체로 mapping을 하기 위해서 Body의 내용을 읽으려고 봤더니(=Stream을 읽기 위해 Stream을 얻었더니) 그 안에 있는 내용을 이미 다 읽어버려서 내용을 더 이상 읽을 수 없는 상태가 된 것!
                - read를 한 번 해버리면 client에서 요청이 오는 것에 대한 내용을 더 이상 읽을 수가 없음(GlobalFilter에서 이미 읽어버렸음)
                - Spring에 controller에다가 JSON body를 전달하려고 했더니 내용이 없는 상황
        - 해결 방법
            - `ContentCachingRequestWrapper` 사용
                - **'캐싱'을 사용하여 내용을 이미 한 번 읽었어도 몇번이고 계속 다시 읽을 수 있게 만듦**
                - 클래스 내부를 확인해보면 `ByteArrayOutputStream cachedContent;`가 존재하는데 여기에다가 내용을 미리 담아두는 것
                    - (이후 Spring이나 누군가가 읽으려고 할 때 여기에 담겨진 내용을 리턴해주게 됨)
                    - 자세히 살펴보면 크기는 정해져 있지만 내용은 복사해두지 않은 상태이기 때문에 chain.doFilter의 후처리 부분에 읽는 코드 구현
                        - Spring이 안에서 모든 것을 mapping한 다음에 읽어야 함
                        - **chain.doFilter가 일어난 후에 request에 대한 정보를 찍어야 함!** (중요)
                - ❗주의❗
                    - '전처리'라고 해서 들어오자마자 내용을 처리할 수 있는 것이 아님
                    - ContentCachingRequestWrapper 생성자가 생성했을 때는 cachedContent에 길이만 저장하고 있지 내용을 담고 있지 않음
                        - 이 때는 read를 하지 않기 때문에 길이만 초기화를 시킴
                    - chain.doFilter()를 통해 실제 내부 Spring 안으로 들어가야 내부의 writeToCache() 메서드가 호출이 됨
                        - 실제로 내부의 writeToCache() 메서드가 호출이 되어야 cachedContent에다가 write()하게 됨!
                        - request에 대한 내용이 ByteArray content에 담기게 되고 그때 우리가 읽을 수 있게 됨!
                    - **핵심 : request에 대한 내용은 chain.doFilter() 이후에 찍어야 함!!**

- 전처리/후처리 모두 구현

    - filter/GlobalFilter.java
        ```java
        @Slf4j
        @Component
        public class GlobalFilter implements Filter {
            @Override
            public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
                
                // ~~ 전처리 구간 ~~

                // url 받기 (*형변환 필요*) - Filter단에서는 Request와 Response에 대해서 변경 시켜줄 수 있음
                // HttpServletRequest : 이미 ServletRequest를 상속받은 클래스, 구현은 이미 되어있기 때문에 인터페이스만 바꿈
                // Cache 기능 사용 - 이미 한 번 읽었더라도 여러번 다시 읽는 것 가능! (HttpServletRequest/Response를 한번 형변환 시켜서 넘겨줌)
                ContentCachingRequestWrapper httpServletRequest = new ContentCachingRequestWrapper((HttpServletRequest)request);
                ContentCachingResponseWrapper httpServletResponse = new ContentCachingResponseWrapper((HttpServletResponse)response);

                String url = httpServletRequest.getRequestURI();
                // ~~ 전처리 구간 ~~

                chain.doFilter(httpServletRequest, httpServletResponse);
                // ~~ 후처리 구간 ~~
                // req
                // content 내용을 byte array로 받고 그것을 다시 문자열 받음
                String reqContent = new String(httpServletRequest.getContentAsByteArray());
                log.info("request url : {}, requestBody : {}", url, reqContent);

                // res
                // response는 Controller를 다 타고 response에 담겨서 옴
                String resContent = new String(httpServletResponse.getContentAsByteArray());
                // 응답 내용들 찍어보기
                int httpStatus = httpServletResponse.getStatus();

                log.info("response status : {}, responseBody : {}", httpStatus, resContent);

                // ~~ 후처리 구간 ~~
            }
        }
        ```

    - Talend API로 POST request 보내기
        - request body
            ```json
            {
            "name" : "steve",
            "age" : 10
            }
            ```

    - console output
        - 정상적으로 출력
            ```
            2021-09-04 11:54:38.833  INFO 28908 --- [nio-8080-exec-1] c.e.filter.controller.ApiController      : User : User(name=steve, age=10) , User(name=steve, age=10)
            2021-09-04 11:54:38.866  INFO 28908 --- [nio-8080-exec-1] com.example.filter.filter.GlobalFilter   : request url : /api/user, requestBody : {
            "name" : "steve",
            "age" : 10
            }
            2021-09-04 11:54:38.867  INFO 28908 --- [nio-8080-exec-1] com.example.filter.filter.GlobalFilter   : response status : 200, responseBody : {"name":"steve","age":10}
            ```
        - 하지만 Response Body에 No Content 발생 (에러!)
            - 이것도 위의 Request 경우와 마찬가지로 먼저 내용을 한 번 읽어버렸기 때문에 (httpServletResponse.getContentAsByteArray()) response body의 커서가 끝까지 내려가서 더 이상 내용이 없는 상황임
            - 따라서 내가 읽은 만큼 다시 한 번 **복사**해주는 것 필요!
                - httpServletResponse.copyBodyToResponse(); 추가

- 전처리/후처리 모두 구현 + request/response 에러 해결

    - filter/GlobalFilter.java
        ```java
        @Slf4j
        @Component
        public class GlobalFilter implements Filter {
            @Override
            public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
                
                // ~~ 전처리 구간 ~~

                // url 받기 (*형변환 필요*) - Filter단에서는 Request와 Response에 대해서 변경 시켜줄 수 있음
                // HttpServletRequest : 이미 ServletRequest를 상속받은 클래스, 구현은 이미 되어있기 때문에 인터페이스만 바꿈
                // Cache 기능 사용 - 이미 한 번 읽었더라도 여러번 다시 읽는 것 가능! (HttpServletRequest/Response를 한번 형변환 시켜서 넘겨줌)
                ContentCachingRequestWrapper httpServletRequest = new ContentCachingRequestWrapper((HttpServletRequest)request);
                ContentCachingResponseWrapper httpServletResponse = new ContentCachingResponseWrapper((HttpServletResponse)response);

                String url = httpServletRequest.getRequestURI();

                // ~~ 전처리 구간 ~~
                chain.doFilter(httpServletRequest, httpServletResponse);
                // ~~ 후처리 구간 ~~
                // req
                // content 내용을 byte array로 받고 그것을 다시 문자열 받음
                String reqContent = new String(httpServletRequest.getContentAsByteArray());
                log.info("request url : {}, requestBody : {}", url, reqContent);

                // res
                // response는 Controller를 다 타고 response에 담겨서 옴
                String resContent = new String(httpServletResponse.getContentAsByteArray());
                // 응답 내용들 찍어보기
                int httpStatus = httpServletResponse.getStatus();

                // 읽은 값 만큼 복사
                httpServletResponse.copyBodyToResponse();

                log.info("response status : {}, responseBody : {}", httpStatus, resContent);

                // ~~ 후처리 구간 ~~
            }
        }
        ```

    ➡ Response Body까지 정상적으로 잘 내려줌
        
## 중간 정리

- Filter를 사용하여 Request/Response 내용을 찍어주고 싶다면...

    1. ContentCachingRequestWrapper/ContentCachingResponseWrapper 클래스를 사용하여 doFilter() 후에 request Body에 있는 내용을 copy해서 찍으면 됨
    2. response의 내용도 동일하게 copy해서 찍되, 반드시 추가적으로 copyBodyToResponse() 메서드를 호출하여 Client가 제대로 된 응답 메시지를 받을 수 있게 해줘야 함!

- Filter 사용 예제 (상황에 따라 구현)
    - Filter를 통해 제일 최전방에서 들어오는 정보들을 볼 수 있음
    - Session 정보를 불러와서 Session에 특정한 정보가 있고 없고를 판단하여 로그아웃을 시키거나 401 unauthorized 에러를 발생시킴
    - logging 용도로 사용

## GlobalFilter를 특정 구역에다 적용시키기

- 서로 다른 URL를 가지는 ApiUserController 클래스 생성
    - url : "/api/temp"
    - 기존 ApiController에만 Filter를 적용시켜 볼 것임
- FilterApplication에 @ServletComponentScan 어노테이션 추가
    - FilterApllication.java
        ```java
        @SpringBootApplication
        @ServletComponentScan
        public class FilterApplication {

            public static void main(String[] args) {
                SpringApplication.run(FilterApplication.class, args);
            }
        }
        ```
- GlobalFilter에 @Component 대신 @WebFilter() 어노테이션으로 변경
    - 그 안에 원하는 request url 패턴을 넣어줌 (ApiController의 url 패턴)
    - `@WebFilter(urlPatterns = "api/user/*")`
        - urlPatterns : 여러 가지 클래스를 String 배열로 넣게 되면, 여러 가지 주소를 설정할 수도 있음!
    - filter/GlobalFilter.java
        ```java
        @Slf4j
        @WebFilter(urlPatterns = "/api/user/*")
        public class GlobalFilter implements Filter {
            @Override
            public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
                // 생략
        }
        ```

- Talend API POST Request
    - http://localhost:8080/api/user 로 요청한 경우
        - Filter를 탔음!
        - console output
            ```
            2021-09-04 12:28:56.036  INFO 24884 --- [nio-8080-exec-7] com.example.filter.filter.GlobalFilter   : request url : /api/user, requestBody : {
            "name" : "steve",
            "age" : 10
            }
            2021-09-04 12:28:56.037  INFO 24884 --- [nio-8080-exec-7] com.example.filter.filter.GlobalFilter   : response status : 200, responseBody : {"name":"steve","age":10}
            ```

    - http://localhost:8080/api/temp 로 요청한 경우
        - Filter를 타지 않음!
        - request Body는 잘 내려주지만 filter에서 log를 찍지는 않음!
        - console output
            ```
            2021-09-04 12:31:01.953  INFO 24884 --- [io-8080-exec-10] c.e.filter.controller.ApiUserController  : Temp : User(name=steve, age=10) , User(name=steve, age=10)
            ```
