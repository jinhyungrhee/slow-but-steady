# Async

## 비동기

- Java 8 CompletableFuture 사용
- 별도의 Thread를 통해서 처리하는 방식
- 깊게 들어가면 끝이 없기 때문에 간단히만 다룸

## 비동기 처리하기

- Async 프로젝트 생성
- AsyncApplication에 `@EnableAsync` 어노테이션 붙임
    - AsyncApplication.java
        ```java
        @SpringBootApplication
        @EnableAsync
        public class AsyncApplication {

            public static void main(String[] args) {
                SpringApplication.run(AsyncApplication.class, args);
            }

        }
        ```

- ApiController에 hello() 메서드 생성
    - AsyncService에 @Async 어노테이션이 없었더라면 asyncService.hello()가 다 끝날때까지 기다렸다가 response가 나갔음
    - 하지만 @Async 어노테이션이 있기때문에 "hello"라는 response를 받고 바로 나감
    - controller/ApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            private final AsyncService asyncService;

            public ApiController(AsyncService asyncService) {
                this.asyncService = asyncService;
            }

            @GetMapping("/hello")
            public String hello(){
                asyncService.hello();
                // AsyncService에 @Async 어노테이션이 없었더라면 asyncService.hello()가 다 끝날때까지 기다렸다가 response가 나갔음
                // 하지만 @Async 어노테이션이 있기때문에 "hello"라는 response를 받고 바로 나감
                System.out.println("method end");
                return "hello";
            }
        }
        ```

- service 패키지에 AsyncService 클래스 생성
    - 비동기로 동작할 수 있도록 @Async 어노테이션 추가
    - service/AsyncService.java
        ```java
        @Service
        public class AsyncService {

            // 비동기로 동작할 수 있도록 @Async 어노테이션 추가
            @Async
            public void hello() {

                for(int i = 0; i < 10; i++){
                    try {
                        Thread.sleep(2000);
                        System.out.println("thread sleep ...");
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
        ```

- Talend API GET request
    - http://localhost:8080/api/hello
    - console
        ```
        method end
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        thread sleep ...
        ```

## Lombok 사용하여 조금 더 자세히 보기

- 이전 프로젝트에서 사용하던 `build.gradle` 내용 복사/붙여넣기
    - configurations
        ```
        configurations {
            compileOnly {
                extendsFrom annotationProcessor
            }
        }
        ```

    - dependencies
        ```
        compileOnly 'org.projectlombok:lombok'
        annotationProcessor 'org.projectlombok:lombok'
        ```

- lombok 사용하기 위해 `@Slf4j` 어노테이션 추가
    - ApiController.java
        ```java
        @Slf4j
        @RestController
        @RequestMapping("/api")
        public class ApiController {

            private final AsyncService asyncService;

            public ApiController(AsyncService asyncService) {
                this.asyncService = asyncService;
            }

            @GetMapping("/hello")
            public String hello(){
                asyncService.hello();
                log.info("method end");
                return "hello";
            }
        }
        ```
    - AsyncService.java
        ```java
        @Slf4j
        @Service
        public class AsyncService {

            @Async
            public void hello() {

                for(int i = 0; i < 10; i++){
                    try {
                        Thread.sleep(2000);
                        log.info("thread sleep ...");
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
        ```
    - 동일한 Talend API GET reqeust
        - console output
            ```
            2021-09-05 12:33:04.532  INFO 11496 --- [nio-8080-exec-1] c.e.async.controller.ApiController       : method end
            2021-09-05 12:33:06.559  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:08.574  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:10.580  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:12.584  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:14.586  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:16.589  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:18.597  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:20.598  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:22.602  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            2021-09-05 12:33:24.603  INFO 11496 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
            ```
            - **별도의 Thread에서 async하게 도는 것을 확인할 수 있음!**

## Response 내려주기

- hello() 메서드에서 String를 리턴시킴
- run() 메서드 추가
    - 이 메서드는 CompletableFuture를 리턴시킴
    - @Async 어노테이션 추가
    - AsyncService.java
        ```java
        @Slf4j
        @Service
        public class AsyncService {

            // 여기는 어노테이션 붙여줌
            @Async
            public CompletableFuture run(){
                
                // completableFuture로 동작함
                return new AsyncResult(hello()).completable();
            }

            public String hello() {

                for(int i = 0; i < 10; i++){
                    try {
                        Thread.sleep(2000);
                        log.info("thread sleep ...");
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                return "async hello";
            }
        }
        ```
- Controller hello() 메서드에서 리턴을 바로 하도록 설계
    - ApiController.java
        ```java
        @Slf4j
        @RestController
        @RequestMapping("/api")
        public class ApiController {
            private final AsyncService asyncService;

            public ApiController(AsyncService asyncService) {
                this.asyncService = asyncService;
            }

            @GetMapping("/hello")
            public CompletableFuture hello(){
                // CompletableFuture : 다른 스레드에서 실행시키고 결과를 반환받는 형태

                log.info("completable future init");

            // Controller에서 리턴을 바로 함
                return asyncService.run();
            }
        }
    ```

- CompletableFuture가 반환형일때 별도의 Thread에서 실행시켜줌
- 결국에 이 작업이 끝나고 나서 "async hello"라는 response 내려줌
    - console
    ```
    2021-09-05 12:44:31.944  INFO 23380 --- [nio-8080-exec-1] c.e.async.controller.ApiController       : completable future init
    2021-09-05 12:44:33.979  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:35.987  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:37.996  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:40.010  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:42.019  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:44.031  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:46.037  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:48.040  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:50.042  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:44:52.045  INFO 23380 --- [         task-1] com.example.async.service.AsyncService   : thread sleep ...
    ```
    - 이 작업이 다 끝나고 나서 response body 내려옴
        ```
        async hello
        ```

- completableFuture 일반적인 사용방법
    - **여러 개의 API를 동시에 전송했을 때 거기에 대한 결과를 Join해서 받을 때 사용**
    - 단계별로 request가 나가는 게 아니라 한 번에 여러 request가 나가고 그것의 결과를 모아서 return할 때 @Async를 사용하는 것 보다는 일반적인 메서드 내에서 CompletablFuture를 여러 개 만든 다음에 전송시키고 합쳐서 응답을 내려주는 게 바람직

- 기본적인 Spring의 Thread 개수
    - 8개 정도 밖에 안 됨
    - 양이 많지 않기 때문에 직접 Thread를 만들어 줄 수 있음

## Thread Pool 지정하기

- 우리가 원하는 Thread를 지정하여 실행시키기
- Thread Pool을 지정하는 것은 환경, Request 양에 따라서 달라짐
    - Pool이 어떻게 동작하는지 정확히 알고 있어야 설정을 할 수 있음!

- config 패키지에 AppCongfig 클래스 생성
    - config/AppConfig.java
    ```java
    @Configuration
    public class AppConfig {

        @Bean("async-thread")
        public Executor asyncThread(){
            ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();
            threadPoolTaskExecutor.setMaxPoolSize(100);
            // CorePoolSize의 10개를 다 쓰게 되면 Queue에 들어가게 됨
            threadPoolTaskExecutor.setCorePoolSize(10);
            // Queue까지 다 차게 되면 CorePoolSize가 원래 크기만큼 한 번더 늘어나게 됨 => 20개 => Queue가 꽉참 => 30개 => ...
            // MAX까지 다 찬 다음에 Queue에 들어가는 것이 아님!
            threadPoolTaskExecutor.setQueueCapacity(10);
            threadPoolTaskExecutor.setThreadNamePrefix("Async-");

            return threadPoolTaskExecutor;
        }
    }
    ```

- AsyncService 클래스에서 우리가 사용할 Thread pool 지정
    - service/AsyncService.java
        ```java
        @Slf4j
        @Service
        public class AsyncService {

            // pool 지정
            // 우리가 원하는 Thread의 Bean이름을 @Async안에 넣어줌
            @Async("async-thread")
            public CompletableFuture run(){
                
                // completableFuture로 동작함
                return new AsyncResult(hello()).completable();
            }

            public String hello() {

                for(int i = 0; i < 10; i++){
                    try {
                        Thread.sleep(2000);
                        log.info("thread sleep ...");
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                return "async hello";
            }
        }
        ```

- console output
    - 우리가 지정한 Thread를 이용한 것 확인 가능!
    ```
    2021-09-05 12:59:25.740  INFO 10796 --- [nio-8080-exec-1] c.e.async.controller.ApiController       : completable future init
    2021-09-05 12:59:27.758  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:29.759  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:31.763  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:33.777  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:35.784  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:37.787  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:39.801  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:41.806  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:43.806  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    2021-09-05 12:59:45.808  INFO 10796 --- [        Async-1] com.example.async.service.AsyncService   : thread sleep ...
    ```


## 정리

- @Async는 AOP기반이기 때문에 Proxy 패턴을 탐
    - 따라서 public 메서드에만 Async를 지정할 수 있음
    - ex) Async로 설정해놓고 이 안에서 hello()를 호출하면 그 부분은 Async가 동작하지 않음
        - 같은 클래스 내에서 같은 메서드를 호출할 때에는 Async를 타지 않음!
        - AsyncService.java
            ```java
            @Slf4j
            @Service
            public class AsyncService {

                @Async("async-thread")
                public CompletableFuture run(){
                    // **주의** Async로 설정해놓고 이 안에서 hello()를 호출하면 그 부분은 Async가 동작하지 않음
                    hello();
                    // **주의**
                    return new AsyncResult(hello()).completable();
                }

                public String hello() {

                    for(int i = 0; i < 10; i++){
                        try {
                            Thread.sleep(2000);
                            log.info("thread sleep ...");
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }

                    return "async hello";
                }
            }
            ```

- Async는 DB나 Spring보다는 웹의 난이도, 아키텍쳐의 난이도가 올라갔을 때 보는 부분임
    - '이런 방법도 있다' 정도만 알아두면 될 듯!
    - Spring MVC에서도 Async를 사용할 수 있다