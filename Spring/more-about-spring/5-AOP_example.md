# AOP 실무 사례

- ❗AOP를 사용하기 위해서는 **Dependency**를 추가해야 함❗
    - Spring에는 수많은 모듈이 존재하는데 거기서 내가 필요한 것만 골라서 사용하면 됨
    - `build.gradle`의 dependencies에 `implementation 'org.springframework.boot:spring-boot-starter-aop'` 추가하고 새로고침(코끼리 그림)해줌
        - 버튼이 안 보일 경우 오른쪽 Gradle 탭에 들어가서 새로고침 버튼 클릭
    ```java
    dependencies {
        implementation 'org.springframework.boot:spring-boot-starter-aop'
        implementation 'org.springframework.boot:spring-boot-starter-web'
        testImplementation 'org.springframework.boot:spring-boot-starter-test'
    }
    ```

- 일반적인 GET/POST 메서드 

    - REST API 컨트롤러 생성

        - aop 프로젝트 아래 'controller' 패키지 생성 - controller 패키지 아래 'RestApiController' 클래스 생성
        - get 메서드와 post 메서드 정의
        - RestApiController.java
            ```java
            @RestController
            @RequestMapping("/api")
            public class RestApiController {
                
                // get 메서드 생성 - path variable, request parameter 하나씩 받음
                @GetMapping("/get/{id}")
                public void get(@PathVariable Long id, @RequestParam String name){
                    System.out.println("get method");
                    System.out.println("get method : "+id);
                    System.out.println("get method : "+name);
                }

                // post 메서드 생성 - Request body로 받음(클래스 객체 dto 필요)
                @PostMapping("/post")
                public void post(@RequestBody User user){
                    System.out.println("post method : "+user);
                }
            }
            ```

    - User 클래스 객체 정의
        - aop/dto 패키지에 User 클래스 생성
        - User.java
            ```java
            // POST에서 Request body로 받을 정보 지정
            public class User {
                private String id;
                private String pw;
                private String email;

                // getter & setter
                public String getId() {
                    return id;
                }

                public void setId(String id) {
                    this.id = id;
                }

                public String getPw() {
                    return pw;
                }

                public void setPw(String pw) {
                    this.pw = pw;
                }

                public String getEmail() {
                    return email;
                }

                public void setEmail(String email) {
                    this.email = email;
                }

                // toString 오버라이딩
                @Override
                public String toString() {
                    return "User{" +
                            "id='" + id + '\'' +
                            ", pw='" + pw + '\'' +
                            ", email='" + email + '\'' +
                            '}';
                }
            }
            ```

- AOP 활용하기 #1 (입력 값 출력 값 로그 찍기 / 디버깅)
    - 우리는 현재 API를 두 개만 정의했지만 실무 서버에서는 수많은 엔드포인트(API) 존재 (많으면 10개 ~ 20개 이상)
    - 엔드포인트가 많을 경우 일일이 다 로그(println())를 찍기 어려움
        - 전체 메서드에 로그를 찍으면 너무 많은 정보들이 출력되므로 자신이 보기 원하는 중요한 부분에만 로그를 남김 
    - **AOP를 이용하면 각 메서드마다 로그를 찍는 부분을 한 곳으로 모을 수 있음!**

    1. aop 패키지 생성 - ParameterAop 클래스 생성
        - ParameterAop.java
            - 클래스 어노테이션
                - AOP로 동작하기 위해서 @Aspect 추가
                - Spring에서 관리되기 위해 @Component 추가
            - 메서드 어노테이션
                - @pointcut : 어느 부분에 적용시킬 것인지 정하는 것 (*굉장히 많은 연산 수식들 존재*)
                    - `"execution()"`에 path로 지정
                    - `* com.example.aop.controller..*.*(..)` : "aop 프로젝트 하위 controller 패키지 하위에 있는 모든 메소드를 다 AOP로 보겠다" 의미
                - @Before : 들어가기 전 (메서드가 실행되기 전) 넘어가는 argument 확인
                    - 'cut() 메서드(pointcut)'가 시작되는 지점에 before때 해당 메서드를 실행시킴
                    - JointPoint(=들어가고 나가는 지점에 대한 정보들을 가지고 있는 객체) 활용
                - @AfterReturning : return될 때 어떤 값이 return되는지 확인
                    - 'cut() 메서드(pointcut)'가 return하는 값 확인
                    - JointPoint(=들어가고 나가는 지점에 대한 정보들을 가지고 있는 객체) 활용
                    - Object를 받을 수 있음 (returning 속성 값으로 해당 Object의 객체를 입력해줘야 함!)
            - 사용된 Method 이름 출력하기
                - `joinPoint`와 `MethodSignature` 클래스 사용
                    1. joinPoint의 getSignature() 사용한 뒤 '형변환(MethodSignature)'
                    2. 형변환 뒤 methodSignature의 getMethod() 사용하여 method 정보(객체) 가져옴
                    3. 출력시 method객체의 getName() 메서드 사용 - 메서드 이름 출력
            ```java
            @Aspect
            @Component
            public class ParameterAop {

                @Pointcut("execution(* com.example.aop.controller..*.*(..))")
                private void cut(){}

                // 1. 들어가기 전 (메서드가 실행되기 전) 넘어가는 argument 확인 : @Before
                @Before("cut()")
                public void before(JoinPoint joinPoint){
                    // 사용한 method 이름 출력
                    MethodSignature methodSignature = (MethodSignature) joinPoint.getSignature();
                    Method method = methodSignature.getMethod();
                    System.out.println(method.getName());

                    // argument(매개변수) 찾기
                    // method에 들어가고 있는 argument(=매개변수)들의 배열
                    Object[] args = joinPoint.getArgs();

                    // for문으로 class type과 value 차례로 출력
                    for(Object obj : args){
                        System.out.println("type : "+obj.getClass().getSimpleName());
                        System.out.println("value : "+obj);

                    }
                }

                // 2. return될 때 어떤 값이 return되는지 확인 : @AfterReturning
                @AfterReturning(value = "cut()", returning = "returnObj")
                public void afterReturn(JoinPoint joinPoint, Object returnObj){
                    System.out.println("return obj");
                    System.out.println(returnObj);
                }
            }
            ```

    2. RestApiController에서 println()대신 parameter값과 return값만으로 로그 찍을 수 있음!
        - 실제 서비스로직에서는 AOP를 사용하여 디버깅함!
        - Controller 패키지 하위에 존재하는 모든 메서드에 pointcut이 걸려있음

        - RestApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class RestApiController {
            
            @GetMapping("/get/{id}")
            public String get(@PathVariable Long id, @RequestParam String name){
                //System.out.println("get method");
                //System.out.println("get method : "+id);
                //System.out.println("get method : "+name);
                // AOP를 사용하면 더 이상 println()으로 일일이 값 찍을 필요 없음

                return id+" "+name;
            }

            @PostMapping("/post")
            public User post(@RequestBody User user){
                //System.out.println("post method : "+user);
                // AOP를 사용하면 더 이상 println()으로 일일이 값 찍을 필요 없음

                return user;
            }
        }
        ```

    3. 출력 결과
        - GET method
            - URL : http://localhost:9090/api/get/100?name=steve
                - Path Varialbe : 100
                - Query Parameter : name = steve
            - console
                ```
                // method
                get 
                // parameter
                type : Long
                value : 100
                type : String
                value : steve
                // return
                return obj
                100 steve
                ```
        
        - POST mehtod
            - request JSON
                ```js
                {
                "id" : "steve",
                "pw" : "1234",
                "email" : "steve@gmail.com"
                }
                ``` 
            - console
            ```
            // method
            post
            // parameter
            type : User
            value : User{id='steve', pw='1234', email='steve@gmail.com'}
            // return
            return obj
            User{id='steve', pw='1234', email='steve@gmail.com'}
            ```

- AOP 활용하기 #2 (메서드 실행시간을 이용해 서버 부하, 서버 상태 로그 찍기)
    - **커스텀 어노테이션** 사용
        - 해당 어노테이션이 설정된 메서드만 기록되도록 함
    
    1. aop패키지에 TimerAop 클래스 생성
        - aop/TimerAop.java
            ```java
            // 특정 메서드의 실행 시간 찍는 용도
            @Aspect
            @Component
            public class TimerAop {

                // pointcut 1 : controller 하위의 메소드들에 걸음
                @Pointcut("execution(* com.example.aop.controller..*.*(..))")
                private void cut(){}

                // Timer로써 동작할 수 있도록 annotaion에 대한 제약을 하나 걸음
                // pointcut 2 : 패키지 하위에 있는 Timer annotation이 설정된 메서드만 로깅할 것
                @Pointcut("@annotation(com.example.aop.annotation.Timer)")
                private void enableTimer(){}

                // 시간을 잴 것이기 때문에 전-후가 필요하지만 @Befor @After로는 Time을 공유할 수가 없음
                // 따라서 @Around 사용! - cut()과 enableTimer() 조건을 같이 쓰겠다는 의미!
                // @Around는 ProceedingJoinPoint 사용
                @Around("cut() && enableTimer()")
                public void around(ProceedingJoinPoint joinPoint) throws Throwable {
                    // Spring StopWatch 클래스 사용
                    StopWatch stopWatch = new StopWatch();
                    stopWatch.start();

                    //ProceedingJoinPoint의 proceed()를 호출하면 실제 메서드가 실행
                    //만약 return type이 있는 경우 Object로 리턴됨!
                    Object result = joinPoint.proceed();

                    stopWatch.stop();

                    System.out.println("total time : "+stopWatch.getTotalTimeSeconds());
                }

            }
            ```

    2. annotation 커스터마이징 (패키지)
        - annotation 패키지 생성하고 그 안에 Timer 어노테이션 생성
        - annotation/Timer.java
            ```java
            // element Type과 Method에 걸 수 있는 annotation
            // Runtime에 돌아가도록 retention 설정
            @Target({ElementType.TYPE, ElementType.METHOD})
            @Retention(RetentionPolicy.RUNTIME)
            public @interface Timer {
            }
            ```
    
    3. RestApiController의 delete메서드에 Timer어노테이션 설정
        - controller/RestApiController.java
            ```java
            @RestController
            @RequestMapping("/api")
            public class RestApiController {

                @GetMapping("/get/{id}")
                public String get(@PathVariable Long id, @RequestParam String name){

                    return id+" "+name;
                }

                @PostMapping("/post")
                public User post(@RequestBody User user){
                    return user;
                }

                // TimerAop에 사용할 delete 메서드 하나 더 생성
                // 우리가 직접 만든 Timer annotation 붙여줌
                @Timer
                @DeleteMapping("/delete")
                public void delete() throws InterruptedException {

                    // delete시 db logic이 2초 걸린다고 가정(예외처리까지 해줌)
                    Thread.sleep(1000 * 2);

                }
            }
            ```

    4. 실행 결과
        - Request URL : http://localhost:9090/api/delete
        - console
            ```
            total time : 2.0444466
            ```


    5. AOP를 사용하지 않은 경우와 비교하기
        - 실질적으로 business logic이 들어가야 할 곳에 크게 상관없는 부가적인 것들이 반복적으로 들어가고 있음 => `횡단 상태`
        - 이러한 반복적이고 부가적인 것들을 바깥으로 빼는 것(**관점지향적**) => `AOP`
            - 서비스 로직에 집중해서 코드를 작성할 수 있게 도와줌
        - controller/RestApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class RestApiController {

            @GetMapping("/get/{id}")
            public String get(@PathVariable Long id, @RequestParam String name){
                // AOP를 사용하지 않는 경우
                StopWatch stopWatch = new StopWatch();
                stopWatch.start();

                // 실제 로직

                stopWatch.stop();
                System.out.println("total time : " + stopWatch.getTotalTimeSeconds());
                
                return id+" "+name;
            }

            @PostMapping("/post")
            public User post(@RequestBody User user){
                // AOP를 사용하지 않는 경우
                StopWatch stopWatch = new StopWatch();
                stopWatch.start();

                // 실제 로직
                
                stopWatch.stop();
                System.out.println("total time : " + stopWatch.getTotalTimeSeconds());
                
                return user;
            }

            // TimerAop에 사용할 delete 메서드 하나 더 생성
            // 우리가 직접 만든 Timer annotation 붙여줌
            @Timer
            @DeleteMapping("/delete")
            public void delete() throws InterruptedException {
                // AOP를 사용하지 않는 경우
                StopWatch stopWatch = new StopWatch();
                stopWatch.start();

                // delete시 db logic이 2초 걸린다고 가정(예외처리까지)
                Thread.sleep(1000 * 2);

                stopWatch.stop();
                System.out.println("total time : " + stopWatch.getTotalTimeSeconds());

            }
        }
        ```

    6. 정리 및 활용 방안
        - 복잡한 로직이 있거나/DB를 사용한다거나/외부 기관과 통신을 할 때 시간 측정을 하고 싶은 경우 AOP를 이용해 @Timer 어노테이션만 붙이면 AOP가 알아서 시간을 찍어줌
        - 활용 방안
            - 찍힌 시간을 DB에 저장 가능
            - 시간 정보 모니터링 하는 곳에 push 가능
            - 서버 제한 시간이 5초인데 초과했을 경우 서버 관리자에게 알림을 보내는 기능구현 가능

- AOP 활용하기 #3 (값의 변환)

    - 암호화된 값이 들어왔을 때 filter나 intercepter를 통해 변환을 시도하면 Tomcat 자체에서 한 번 Body를 읽어오면 더 이상 읽을 수 없도록 막아놓았기 때문에 변환이 어려움
    - AOP 구간은 이미 fiter와 intercepter를 지나서 값 자체가 객체화 되었기 때문에 그 값을 우리가 변환해주거나 AOP에서 특정한 객체를 넣어줄 수 있음!
        - 외부에서 암호화된 파일이나 필드가 들어올 경우, 그 부분을 코드에서 복호화하는 것이 아니라 이미 AOP단에서 복호화가 완료된 상태에서 들어오게 할 수 있음
        - 반대로 밖으로 내보낼 때, 내부 코드에서는 일반적으로 코딩을 하지만 특정 회원사나 특정 서버에 보낼 때에는 AOP단에서 변경시켜주도록 할 수 있음 (?)

    1. Decode annotation 생성
        - annotation/Decode.java
        ```java
        // element Type과 Method에 걸 수 있는 annotation
        // Runtime에 돌아가도록 retention 설정
        @Target({ElementType.TYPE, ElementType.METHOD})
        @Retention(RetentionPolicy.RUNTIME)
        public @interface Decode {
        }
        ```

    2. PUT API 추가
        - RestApiController.java
        ```java
        @RestController
        @RequestMapping("/api")
        public class RestApiController {

            @GetMapping("/get/{id}")
            public String get(@PathVariable Long id, @RequestParam String name){
                return id+" "+name;
            }

            @PostMapping("/post")
            public User post(@RequestBody User user){
                return user;
            }

            @Timer
            @DeleteMapping("/delete")
            public void delete() throws InterruptedException {
                Thread.sleep(1000 * 2);

            }
            // put 메서드 추가
            // 값을 바꿔줘야 하기 때문에 새로 만든 Decode 어노테이션 사용
            @Decode
            @PutMapping("/put")
            public User put(@RequestBody User user){
                System.out.println("put");
                System.out.println(user);
                return user;
            }
        }
        ```

    3. DecodeAop 추가
        - 이렇게 설계하면 실질적인 controller 코드에서는 User라는 객체를 디코딩할 일이 없게 됨!
        - 이러한 기능들을 enableDecode라는 어노테이션을 통해 진행
        - aop/DecodeAop.java
        ```java
        @Aspect
        @Component
        public class DecodeAop {

            // pointcut 1 : controller 하위의 메소드들에 걸음
            @Pointcut("execution(* com.example.aop.controller..*.*(..))")
            private void cut(){}

            // Decoder로서 동작할 수 있도록 annotaion에 대한 제약을 하나 걸음
            // pointcut 2 : 패키지 하위에 있는 Decode annotation이 설정된 메서드만 로깅할 것
            @Pointcut("@annotation(com.example.aop.annotation.Decode)")
            private void enableDecode(){}

            // 값 찾기 - 전/후
            // 전 : Decode해서 들어가기
            @Before("cut() && enableDecode()")
            public void before(JoinPoint joinPoint) throws UnsupportedEncodingException {
                // enableDecode() -> annotation 붙은 것 찾아냄
                // 어떻게 객체를 찾아서 어떻게 바꿔줄 것인가?
                // 메서드에 넘어가는 argument 찾기 - 특정 객체에 관한 특정 변수
                Object[] args = joinPoint.getArgs();

                for(Object arg : args){
                    // 내가 원하는 객체(User)만 골라내기
                    if(arg instanceof User){
                        // 원하는 객체를 찾았으면 값을 바꿔주기(Decode)
                        // args를 돌다가 내가 원하는 User클래스가 매칭이 되면 해당 값을 User클래스로 형변환(?)
                        User user = User.class.cast(arg);

                        // 기존의 encoding 되어있던 email 정보를 가져옴(Base64)
                        String base64Email = user.getEmail();
                        // [디코딩] Base64.getDecoder().decode() : String 입력 Byte 반환 -> new String()으로 String 객체 생성
                        String email = new String(Base64.getDecoder().decode(base64Email),"UTF-8");
                        // decode된 email을 다시 user Email에 set
                        user.setEmail(email);

                        // <정리> 처음에 들어왔을 때 인코딩된 Base64를 decode해서 다시 set

                    }
                }

            }
            // 후 : Encode해서 내보내기
            @AfterReturning(value = "cut() && enableDecode()", returning = "returnObj")
            public void afterReturn(JoinPoint joinPoint, Object returnObj){
                // 내가 원하는 객체(User)만 골라내기
                if(returnObj instanceof User){
                    //before()과 반대로 진행
                    // returnObj를 형변환시킴
                    User user = User.class.cast(returnObj);
                    // 기존의 decoding 되어있던 email 정보를 가져옴
                    String email = user.getEmail();
                    // [인코딩] Base64.getEncoder().encodeToString(): Byte 입력 String 반환 (.getBytes()로 byte값 입력)
                    String base64Email = Base64.getEncoder().encodeToString(email.getBytes());
                    // encode된 email을 다시 user Email에 set
                    user.setEmail(base64Email);

                    // <정리> returnObj에서 User를 찾아서 평문 email을 인코딩해서 다시 set을 해주고 리턴
                }
            }
        }
        ```

    4. AopApplication을 통해 미리 base64 값 찍어보기
        - AopApplication.java
            ```java
            @SpringBootApplication
            public class AopApplication {

                public static void main(String[] args) {

                    SpringApplication.run(AopApplication.class, args);
                    // 먼저 base64 값 찍어보기
                    System.out.println(Base64.getEncoder().encodeToString("steve@gmail.com".getBytes()));
                }
            }
            ```
        - 결과
            - `c3RldmVAZ21haWwuY29t`
            - request 보낼 때 사용
                - 우리의 목표는 Base64로 request가 들어왔을 때 비즈니스 로직(서비스 로직) 내부에서 복호화/암호화하지 않아도 AOP와 annotation만 사용하면 알아서 복호화/암호화가 진행되고 response도 다시 Base64로 보내주는 것

    5. Talend API로 보내기
        - 1)DecodeAop에서 처음에 들어올 때 인코딩된 Base64를 decode해서 다시 setting (before())
        - 2)나갈 때 마찬가지로 평문 Email을 인코딩해서 Base64로 다시 setting
        - 그 결과 실질적으로 통신했을 때 Base64로 보내더라도 response도 Base64의 형태를 유지함!
            - Talend Request Body
                ```json
                {
                "id" : "steve",
                "pw" : "1234",
                "email" : "c3RldmVAZ21haWwuY29t"
                }
                ```
            - Talend Response Body
                ```json
                {
                "id": "steve",
                "pw": "1234",
                "email": "c3RldmVAZ21haWwuY29t"
                }
                ```
    
    6. 정리
        - 실제로 많이 사용되는 예제는 아니지만 특정 회사나 파트너사가 이런식으로 암호화/복호화 요구를 할 수 있음
        - 이때 이러한 코드를 비즈니스 로직에 녹일 수도 있지만 
        - 그것보다는 어노테이션으로 구분을 해서 미리 선처리/후처리를 통해 AOP에서 처리하는 것 가능!
            - 이렇게 구분하면 실질적인 서비스 로직에서 Email은 계속 평문으로 들어있기 때문에 (변경없이) 동일한 로직에 태워서 사용할 수 있음!


### @Component와 @Bean의 차이

    - @Bean은 클래스에 붙일 수 없음
        - @Bean은 메소드 단위로 사용하는 annotation
        - @Configuration을 통해 하나의 클래스에 여러 가지 Bean을 등록할 수 있음!
    - @Component를 통해 클래스 단위로 Bean을 등록시킬 수 있으