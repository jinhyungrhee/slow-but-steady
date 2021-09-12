# Interceptor

## Interceptor란?

- Filter와 매우 유사한 형태로 존재
- 차이점은 Spring Context에 등록되기 때문에 Spring에 대한 기능들을 활용할 수 있음
    - 이미 Controller Mapping까지 이루어져 있기 때문에 그 다음에 어떤 메서드를 사용하는지에 대한 정보를 가지고 있을 수 있음
    - Filter는 WebApplication에 등록되기 때문에 Spring context에 대한 내용은 사용할 수 없음
- 주로 **인증 단계**를 처리하거나, Logging하는 데 사용
    - 순수한 내용을 찍기 위해서는 Filter logging 사용
- 선처리/후처리 가능
- Service business logic과 분리시킴으로써 Service 단에서 정말 순수한(인증까지 모두 통과된) request가 넘어가도록 하고 그렇지 않은 것들은 미리 걸러내는 역할을 수행
- 실제로 Controller와 같은 영역 안에 존재함!
    - 그래서 어떤 Controller HandlerMapping이 되었는지도 Interceptor는 알 수 있음
    - Handler를 통해 권한을 확인하는 방법 有

## Interceptor로 Auth 기능 구현하기

-  컨트롤러에 Auth 어노테이션이 붙어 있으면 세션을 검사해서 있을 때만 통과시키고 없으면 통과시키지 않음!

- 두 개의 컨트롤러 생성
    1. 권한 없는 사람도 접근이 가능한 Public Controller
        ```java
        // 아무런 권한이 없는 사용자도 들어올 수 있는 Controller
        // 아무나 사용할 수 있는 Open API 형태
        @RestController
        @RequestMapping("/api/public")
        public class PublicController {
            
            @GetMapping("/hello")
            public String hello(){
                return "public hello";
            }

        }
        ```
    2. 권한 있는 사람만 접근 가능한 Private Controller
        ```java
        // 세션이 인증된 사용자만 넘김
        // 권한 차이 필요 - 어노테이션을 기반으로 활용
        @RestController
        @RequestMapping("/api/private")
        @Auth
        @Slf4j
        public class PrivateController {

            @GetMapping("/hello")
            public String hello(){
                log.info("private hello controller");
                return "private hello";
            }
        }
        ```

- Auth 어노테이션 생성
    - annotatino/Auth.java
        ```java
        @Documented
        @Retention(RetentionPolicy.RUNTIME)
        @Target({ElementType.TYPE, ElementType.METHOD})
        public @interface Auth {
        }
        ```

- AuthInterceptor 생성
    - HandlerInterceptor 상속받음
    - 구현해야 하는 preHandle() 메서드 오버라이딩
    - Spring에 의해 관리되어야 하므로 @Component 어노테이션 붙임
    - ❗알아두기❗
        - (애초에 filter 단에서 cache를 해서 넘겼다면) Global Filter에서 ContentCachingRequest를 만들어서 doFilter()에 넣어주면, 동일한 프로젝트의 Interceptor에서는 들어온 request를 형변환시켜줄 수 있음! 
            - ex) (ContentCachingRequestWrapper) request;
        - 만약 filter 단에서 변경한 reqeust를 doFilter()에서 넣어주지 않았다면 Interceptor에서 request 형변환 실패!
            - filter 단에서 request를 안쪽으로 넣어주는데 filter에서 ContentCachingRequest를 만들어서 request로 넘겨주게 되면 Interceptor에서 당연히 형변환이 가능
            - 그렇지 않고 filter 단에서 HttpServletRequest 형태로 넘어가게 되면 형변환이 불가능하게 됨
    - request를 찍을 때 가장 중요한 것은 `Handler`임! (Hanlder에 매칭됨)
        - Type, formatting, Model, Service 등의 정보들을 가지고 있음
        - ControllerHandlerMApping이 어떤 ControllerHandlerMApping이 되는지 정보를 가짐
    - interceptor/AuthInterceptor.java
        ```java
        // log 사용하기 위해 @Slf4j 붙임
        @Slf4j
        @Component
        public class AuthInterceptor implements HandlerInterceptor {

            @Override
            public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
                String url = request.getRequestURI();
                // body 내용도 찍을 수 있지만 cache를 하지 않았다면 문제 발생!
                // 다른 프로젝트라도 여기에서 request/response body를 읽으면 해당 내용이 손실됨!

                // request를 찍을 때 가장 중요한 것은 Handler!
                log.info("request url : {}", url);

                // interceptor의 핵심 - 마지막에 false 리턴(false면 동작하지 않음!)
                return false;
            }
            // 어노테이션이 달려있는지 체크
            private boolean checkAnnotation(Object handler, Class clazz){
                // resource(javascript, html)에 대한 요청은 무조건 통과시킴 -> 권한 확인X
                if(handler instanceof ResourceHttpRequestHandler){
                    return true;
                }

                // annotation check
                HandlerMethod handlerMethod = (HandlerMethod) handler;

                if(null != handlerMethod.getMethodAnnotation(clazz) || null != handlerMethod.getBeanType().getAnnotation(clazz)){
                    // Auth annotation이 있을 때는 true
                    return true;
                }

                return false;
            };
        }
        ```

- interceptor 등록
    - config 패키지 - MvcConfig 클래스 생성
        ```java
        // @RequiredArgsConstructor -> final로 선언된 객체들을 생성자에서 주입받을 수 있도록 해줌
        // Structure - MvcConfig(AuthInterceptor) 생성자 확인 가능
        @Configuration
        @RequiredArgsConstructor
        public class MvcConfig implements WebMvcConfigurer {
            
            // AuthInterceptor에서 @AutoWired로 자기자신을 넣을 수도 있지만 순환참조가 발생할 수 있기 때문에
            // @RequiredArgsConstructor로 생성자에서 주입받도록 함
            private final AuthInterceptor authInterceptor;

            // 여기에 interceptor 등록
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(authInterceptor);
            }
        }
        ```

- Talend API GET request
    - http://localhost:8080/api/private/hello
    - 통신은 정상적으로 되었지만 console과 response body에 `log.info("private hello controller");` 내용이 제대로 찍히지 않았음
    - 이유
        - request가 들어와서 interceptor에서 return true가 되어야 안으로 들어갈 수 있는데 false이기 때문에 바로 리턴된 것!
        - return true로 바꿔주기!
            ```java
            @Slf4j
            @Component
            public class AuthInterceptor implements HandlerInterceptor {

                @Override
                public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
                    String url = request.getRequestURI();
                    // body 내용도 찍을 수 있지만 cache를 하지 않았다면 문제 발생!
                    // 다른 프로젝트라도 여기에서 request/response body를 읽으면 해당 내용이 손실됨!

                    // request를 찍을 때 가장 중요한 것은 Handler!
                    log.info("request url : {}", url);

                    // interceptor의 핵심 - 마지막에 false 리턴(false면 동작하지 않음!)
                    // true가 되어야 interceptor를 넘어서서 안의 logic을 탈 수 있음
                    // false면 리턴이 됨
                    return true;
                }
            ```
        - 수정 결과
            - console
                ```
                2021-09-04 13:45:14.628  INFO 2796 --- [nio-8080-exec-1] c.e.i.interceptor.AuthInterceptor        : request url : /api/private/hello
                2021-09-04 13:45:14.638  INFO 2796 --- [nio-8080-exec-1] c.e.i.controller.PrivateController       : private hello controller
                ```
            - response body (status code:200)
                `private hello` 


- 권한 체크 추가
    ```java
    @Slf4j
    @Component
    public class AuthInterceptor implements HandlerInterceptor {

        @Override
        public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
            String url = request.getRequestURI();
            // body 내용도 찍을 수 있지만 cache를 하지 않았다면 문제 발생!
            // 다른 프로젝트라도 여기에서 request/response body를 읽으면 해당 내용이 손실됨!

            // request를 찍을 때 가장 중요한 것은 Handler!
            log.info("request url : {}", url);
            // 권한 체크
            boolean hasAnnotation = checkAnnotation(handler, Auth.class);
            log.info("has annotation : {}", hasAnnotation);
            // 조건 : 나의 서버는 모두 public으로 동작을 하는데
            // 단! Auth 권한을 가진 요청에 대해서는 세션, 쿠키 등을 보겠다
            if(hasAnnotation){ // annotatino을 가진 클래스라면
                // 권한 체크
                
            }

            
            // interceptor의 핵심 - 마지막에 false 리턴(false면 동작하지 않음!)
            //return false;
            return true;
        }
    ```

- request 결과
    - private(http://localhost:8080/api/private/hello)
        ```
        2021-09-04 13:49:02.307  INFO 28888 --- [nio-8080-exec-1] c.e.i.interceptor.AuthInterceptor        : request url : /api/private/hello
        2021-09-04 13:49:02.310  INFO 28888 --- [nio-8080-exec-1] c.e.i.interceptor.AuthInterceptor        : has annotation : true
        2021-09-04 13:49:02.316  INFO 28888 --- [nio-8080-exec-1] c.e.i.controller.PrivateController       : private hello controller
        ```
    - public(http://localhost:8080/api/public/hello)
        ```
        2021-09-04 13:50:52.474  INFO 28888 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : request url : /api/public/hello
        2021-09-04 13:50:52.474  INFO 28888 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : has annotation : false
        ```
        
- Query 값을 확인하여 권한 체크
    - AuthInterceptor.java
    ```java
    @Slf4j
    @Component
    public class AuthInterceptor implements HandlerInterceptor {

        @Override
        public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
            String url = request.getRequestURI();
            // body 내용도 찍을 수 있지만 cache를 하지 않았다면 문제 발생!
            // 다른 프로젝트라도 여기에서 request/response body를 읽으면 해당 내용이 손실됨!

            // 쿼리까지 같이 가져옴
            URI uri = UriComponentsBuilder.fromUriString(request.getRequestURI()).query(request.getQueryString()).build().toUri();

            // request를 찍을 때 가장 중요한 것은 Handler!
            log.info("request url : {}", url);
            // 권한 체크
            boolean hasAnnotation = checkAnnotation(handler, Auth.class);
            log.info("has annotation : {}", hasAnnotation);

            // 조건 : 나의 서버는 모두 public으로 동작을 하는데
            // 단! Auth 권한을 가진 요청에 대해서는 세션, 쿠키 등을 보겠다
            if(hasAnnotation){ // annotatino을 가진 클래스라면
                // 권한 체크
                String query = uri.getQuery();
                // 쿼리 내용 출력
                log.info("query : {}", query);
                // 쿼리가 내용이 "name=steve"일때만 통과(true) 아니면 false 리턴
                if(query.equals("name=steve")){
                    return true;
                }

                return false;
            }


            // interceptor의 핵심 - 마지막에 false 리턴(false면 동작하지 않음!)
            //return false;
            return true;
        }
        // 어노테이션이 달려있는지 체크
        private boolean checkAnnotation(Object handler, Class clazz){
            // resource(javascript, html)에 대한 요청은 무조건 통과시킴 -> 권한 확인X
            if(handler instanceof ResourceHttpRequestHandler){
                return true;
            }

            // annotation check
            HandlerMethod handlerMethod = (HandlerMethod) handler;

            if(null != handlerMethod.getMethodAnnotation(clazz) || null != handlerMethod.getBeanType().getAnnotation(clazz)){
                // Auth annotation이 있을 때는 true
                return true;
            }

            return false;
        };
    }
    ```

- Talend API GET request
    - http://localhost:8080/api/private/hello?name=steve
    - console
        ```
        2021-09-04 14:02:36.492  INFO 12264 --- [nio-8080-exec-1] c.e.i.interceptor.AuthInterceptor        : request url : /api/private/hello
        2021-09-04 14:02:36.494  INFO 12264 --- [nio-8080-exec-1] c.e.i.interceptor.AuthInterceptor        : has annotation : true
        2021-09-04 14:02:36.494  INFO 12264 --- [nio-8080-exec-1] c.e.i.interceptor.AuthInterceptor        : query : name=steve
        2021-09-04 14:02:36.500  INFO 12264 --- [nio-8080-exec-1] c.e.i.controller.PrivateController       : private hello controller
        ```
    - response body
        ```
        private hello
        ```
    - 만약 query에 다른 값이 들어온다면 제대로 동작하지 않음
        - http://localhost:8080/api/private/hello?name=john
        - console
            ```
            2021-09-04 14:02:36.500  INFO 12264 --- [nio-8080-exec-1] c.e.i.controller.PrivateController       : private hello controller
            2021-09-04 14:05:46.884  INFO 12264 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : request url : /api/private/hello
            2021-09-04 14:05:46.885  INFO 12264 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : has annotation : true
            2021-09-04 14:05:46.885  INFO 12264 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : query : name=john
            ```
        - response body
            ```
            No contents
            ```

- 특정 URL에 대해서만 검사하고 싶은 경우(추가/제외)
    - MvcConfig에서 addPathPatterns() 사용 (<->excludePathPatterns())
    - MvcConfig.java
        ```java
        @Configuration
        @RequiredArgsConstructor
        public class MvcConfig implements WebMvcConfigurer {
            
            // AuthInterceptor에서 @AutoWired로 자기자신을 넣을 수도 있지만 순환참조가 발생할 수 있기 때문에
            // @RequiredArgsConstructor로 생성자에서 주입받도록 함
            private final AuthInterceptor authInterceptor;

            // 여기에 interceptor 등록
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(authInterceptor).addPathPatterns("/api/private/*");
            }
        }
        ```
    - 굳이 어노테이션을 사용하지 않더라도 Url이 지정된 곳에서만 동작함
    - 지금은 private에서만 동작하도록 지정

    - Talend API GET request
        - http://localhost:8080/api/public/hello?name=bbb 
        - console (인터셉트 동작X)
            ```
            2021-09-04 14:10:26.001  INFO 20516 --- [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
            2021-09-04 14:10:26.001  INFO 20516 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
            2021-09-04 14:10:26.002  INFO 20516 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 0 ms
            ```
        - http://localhost:8080/api/private/hello?name=bbb 
        - conosle (인터셉트 동작O)
            ```
            2021-09-04 14:10:26.001  INFO 20516 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
            2021-09-04 14:10:26.002  INFO 20516 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 0 ms
            2021-09-04 14:11:28.883  INFO 20516 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : request url : /api/private/hello
            2021-09-04 14:11:28.887  INFO 20516 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : has annotation : true
            2021-09-04 14:11:28.887  INFO 20516 --- [nio-8080-exec-3] c.e.i.interceptor.AuthInterceptor        : query : name=bbb
            ```
            - "name=steve"가 아니라 통과가 안 된 것!

- Auauthroized 메시지 보내기
    - AuthException 정의
        - exception/authException.java
            ```java
            package com.example.interceptor.exception;

                public class AuthException extends RuntimeException{
                }
            ```
    - exceptionHandelr 정의
        - handler/GlobalExceptionHandler.java
            ```java
            @RestControllerAdvice
            public class GlobalExceptionHandler {
                @ExceptionHandler(AuthException.class)
                public ResponseEntity authExecption(){
                    return ResponseEntity.status(HttpStatus.UNAUTHORIZED).build();
                }
            }
            ```
    - interceptor에서 권한이 없으면 throw 시킴(AuthException 터뜨림!)
        - AuthInterceptor.java
            ```java
            @Slf4j
            @Component
            public class AuthInterceptor implements HandlerInterceptor {

                @Override
                public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
                    String url = request.getRequestURI();
                    URI uri = UriComponentsBuilder.fromUriString(request.getRequestURI()).query(request.getQueryString()).build().toUri();

                    log.info("request url : {}", url);
                    boolean hasAnnotation = checkAnnotation(handler, Auth.class);
                    log.info("has annotation : {}", hasAnnotation);

                    if(hasAnnotation){
                        // 권한 체크
                        String query = uri.getQuery();

                        log.info("query : {}", query);
                        // 쿼리가 내용이 "name=steve"일때만 통과(true) 아니면 false 리턴
                        if(query.equals("name=steve")){
                            return true;
                        }
                        // ** 권한 없는 경우 false 리턴 대신 예외처리**
                        throw new AuthException();
                    }
            ```
    ➡ 권한이 없는 경우 false 리턴 대신 AuthException을 터뜨림  
    ➡ AuthException 터지면 Handler(GlobalExceptionHandler)가 받아서 UNAUTHORIZED status code 401를 내려줌


## 정리

-  registry.addInterceptor()를 통해 여러 가지 interceptor를 등록할 수 있고 등록된 순서대로 타게 되어있음
    - 인증의 과정도 여러가지로 depth를 두고 활용할 수 있음!

- 필터와의 차이점
    - 인터셉터
        - spring context에서 관리
        - annotation, class에 해당하는 기능들 사용 가능
    - 필터
        - web application에서 관리
            - hanlder라는 object가 없음!