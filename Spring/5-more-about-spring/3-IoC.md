# IoC

- IoC(Inversion of Control)

    - IoC는 Spring Container에서 관리하기 때문에 Spring 프로젝트로 만듦
    - 개발자가 직접 관리했던 Encoder를 Spring Container에 넘겨줌
        - Main.java 제외하고 ioc 프로젝트에서 만들었던 모든 것 복사/붙여넣기
    - Spring Container는 생성된 객체들을 다 가져가고 그것들의 생명주기를 관리함

- 여전히 개발자가 직접 객체를 생성하고 주입시키고 있음

    - ioc project/Main.java
    ```java
        public class Main {

            public static void main(String[] args) {
                String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                // DI : main에서 주입해서 사용
                // Encoder 클래스를 수정하지 않아도 Base64로 작동 -> 넘겨주는 주입 객체만 변경! (외부에서 사용하는 객체를 주입받는 형태)
                Encoder encoder = new Encoder(new UrlEncoder());
                String result = encoder.encode(url);

                System.out.println(result);
            }
        }
        ```

- Spring에게 관리를 해달라고 요청하는 어노테이션

    - `@Component`
    - Spring Bean으로 만들어 관리를 해줌
    - Spring이 실행될 때 `@Component` 어노테이션이 붙은 클래스를 찾아서 직접 객체를 Singleton 형태로 만들어서 Spring Container에서 관리함
        ```java
        import org.springframework.stereotype.Component;
        import java.util.Base64;

        @Component
        public class Base64Encoder implements IEncoder {

            public String encode(String message) {
                return Base64.getEncoder().encodeToString(message.getBytes());
            }
        }
        ```

- Spring Container에서 객체를 꺼내어 쓰는 방법

    - SpringApplicationContext를 사용하여 객체를 가져옴
    - ApplicationContextProvider.java
        ```java
        import org.springframework.beans.BeansException;
        import org.springframework.context.ApplicationContext;
        import org.springframework.context.ApplicationContextAware;
        import org.springframework.stereotype.Component;

        @Component
        public class ApplicationContextProvider implements ApplicationContextAware {

            private static ApplicationContext context;

            // set 메서드
            // 이것(ApplicationContext) 또한 웹으로부터 주입을 받는 것임 - Spring이 알아서 처리
            @Override
            public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
                // 주입받은 것을 static 변수에 할당
                context = applicationContext;
            }

            // 주입받은 것을 가져다 쓰는 static get 함수 생성
            public static ApplicationContext getContext(){
                return context;
            }
        }
        ```

    - Encoder에 set 메서드 생성
        - Bean을 주입받을 수 있는 장소 1) 변수 생성자  2) set 메서드
        - Encoder.java
            ```java
            public class Encoder {

                private IEncoder iEncoder;

                // DI : 생성자에서 인터페이스 받아서 사용
                public Encoder(IEncoder iEncoder) {
                    this.iEncoder = iEncoder;
                }

                // set 메서드 생성 - Bean을 주입받을 수 있는 장소 : 1) 변수 생성자  2) set 메서드
                public void setIEncoder(IEncoder iEncoder){
                    this.iEncoder = iEncoder;
                }

                public String encode(String message) {
                    // iEncoder를 통해 encode 호출
                    return iEncoder.encode(message);

                }
            }
            ```

    - IoC(제어의 역전)
        - Bean을 통해 객체 주입받기
        - IocApplication.java (Main)
            ```java
            import org.springframework.boot.SpringApplication;
            import org.springframework.boot.autoconfigure.SpringBootApplication;
            import org.springframework.context.ApplicationContext;

            @SpringBootApplication
            public class IocApplication {

                public static void main(String[] args) {
                    // SpringApplication 실행
                    SpringApplication.run(IocApplication.class, args);
                    // 주입받은 application context 가져옴
                    ApplicationContext context = ApplicationContextProvider.getContext();

                    
                    // *주입*
                    // DI는 해주지만 IoC(객체관리)는 new로 해주지 않을 것임! -> Bean으로 객체 찾아오기

                    // Bean 찾는 방법(클래스 타입)
                    Base64Encoder base64Encoder = context.getBean(Base64Encoder.class);
                    UrlEncoder urlEncoder = context.getBean(UrlEncoder.class);

                    // Base64Encoder 주입
                    Encoder encoder = new Encoder(base64Encoder);
                    String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                    // Base64 인코딩 출력
                    String result = encoder.encode(url);
                    System.out.println(result);
                    
                    // set메서드로 urlEncoder 주입
                    encoder.setIEncoder(urlEncoder);
                    
                    // url 인코딩 출력
                    result = encoder.encode(url);
                    System.out.println(result);
                }

            }
            ```

- Encoder도 Bean으로 만들기
    - Encoder 클래스에 @Component 어노테이션 붙이는 순간 에러 발생
        - Bean이 한 개만 존재할 경우 바로 매칭이 되지만 여러 개일 경우(Base64Encoder, UrlEncoder) Spring에서 어떤 것을 매칭시킬지 결정하지 못함
        - `@Qualifier("Bean이름")` 어노테이션 사용하여 특정 Bean을 지정해줘야함!
            ```java
            @Component
            public class Encoder {

                private IEncoder iEncoder;

                // @Qualifier => 나는 "urlEncoder"를 사용하겠다 지정!
                // 1) 이름은 클래스명 맨 첫자 소문자로 바꿔서 사용 가능 (Base64Encoder -> "base64Encoder")
                // 2) @Component("이름")으로 지정해서 사용 가능
                public Encoder(@Qualifier("base64Encoder") IEncoder iEncoder) {
                    this.iEncoder = iEncoder;
                }

                public void setIEncoder(IEncoder iEncoder){
                    this.iEncoder = iEncoder;
                }

                public String encode(String message) {
                    return iEncoder.encode(message);
                }
            }
            ```
    
    - Encoder도 Bean으로 만들면 Main에서 new를 쓸 일이 사라짐
    - IocApplication.java (Main)
        ```java
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.context.ApplicationContext;

        @SpringBootApplication
        public class IocApplication {

            public static void main(String[] args) {
                SpringApplication.run(IocApplication.class, args);
                ApplicationContext context = ApplicationContextProvider.getContext();

                
                // *주입*
                // DI는 해주지만 IoC(객체관리)는 new로 해주지 않을 것임! -> Bean으로 객체 찾아오기

                // Encoder 자체를 Bean으로 만들면 더이상 여기에서 불러올 필요가 없음!
                //Base64Encoder base64Encoder = context.getBean(Base64Encoder.class);
                //UrlEncoder urlEncoder = context.getBean(UrlEncoder.class);

                // Base64Encoder 주입
                // Encoder 자체를 Bean으로 만들었으므로 바로 getBean으로 가져오기 가능! (Encoder 클래스에서 타입 변경, 이미 Encoder는 base64가 주입된 상태임)
                Encoder encoder = context.getBean(Encoder.class);
                String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                String result = encoder.encode(url);
                System.out.println(result);
            }

        }
        ```

        - **이제는 모든 권한이 Spring에게 넘어간 상태임!**
            - Spring Conatiner에서 관리되는 객체들을 `Bean`이라고 부름
                - *특정 클래스에서 new로 생성된 객체가 Bean이라고 쉽게 생각해도 됨*
            - 이제 모든 객체들이 Spring Container 안에서 Bean으로 관리되는 상태가 되었음
            - 단순하게 annotation(@Qualifier)만 붙여서 Spring으로부터 주입을 받아서 사용함


- 두 개의 Encoder를 사용하고 싶은 경우
    - Encoder를 @Component로 등록하지 않고 직접 Bean으로 등록하기
    - Main에 또 다른 클래스(AppConfig클래스) 생성 후 `@Configuration` annotation 등록
        - @Configuration : 한 개의 클래스에서 여러 개의 Bean을 등록하는 경우 사용!
        - @Configuration도 내부에 @Componenet를 가지고 있으므로 @Component와 동일한 역할 수행

    - Encoder 클래스는 더 이상 자체로 Bean은 아님
    - Encoder.java
        ```java
        public class Encoder {

            private IEncoder iEncoder;

            // DI : 생성자에서 인터페이스 받아서 사용
            public Encoder(IEncoder iEncoder) {
                this.iEncoder = iEncoder;
            }

            // set 메서드 생성 - Bean을 주입받을 수 있는 장소 : 1) 변수 생성자  2) set 메서드
            public void setIEncoder(IEncoder iEncoder){
                this.iEncoder = iEncoder;
            }

            public String encode(String message) {
                // iEncoder를 통해 encode 호출
                return iEncoder.encode(message);

            }
        }
        ```

    - 하지만 Main에서 AppConfig 클래스에서 Encoder 클래스의 객체들을 여러 개의 Bean으로 만들어 관리함
    - 이 경우 이름으로 Bean을 가져와야 함! (동일한 클래스에서 생성된 Bean이기 때문)
    - IocApplication.java (Main)
        ```java
        @SpringBootApplication
        public class IocApplication {

            public static void main(String[] args) {
                // SpringApplication 실행
                SpringApplication.run(IocApplication.class, args);
                // 주입받은 application context 가져옴
                ApplicationContext context = ApplicationContextProvider.getContext();

                
                // *주입*
                // DI는 해주지만 IoC(객체관리)는 new로 해주지 않을 것임! -> Bean으로 객체 찾아오기

                // Encoder 클래스의 객체를 AppConfig 클래스 안에서 Bean으로 만들어 관리하고 있기 때문에 이름으로 Bean을 가져올 수 있음
                Encoder encoder = context.getBean("urlEncode",Encoder.class);
                String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                String result = encoder.encode(url);
                System.out.println(result);
            }

        }

        // 한 개의 클래스에서 여러 개의 Bean 등록 가능
        @Configuration
        class AppConfig{

            // 개발자가 직접 만들더라도 코드 내에서 new로 생성해서 사용하는 것이 아니라 미리 Bean을 등록해서 사용
            @Bean("base64Encode")
            public Encoder encoder(Base64Encoder base64Encoder){
                // Base64Encoder를 spring으로부터 주입받아서 새로운 객체 생성해 리턴
                return new Encoder(base64Encoder);
            }

            // 각각의 Bean을 구분하기 위해 "이름" 설정
            @Bean("urlEncode")
            public Encoder encoder(UrlEncoder urlEncoder){
                // UrlEncoder를 spring으로부터 주입받아서 새로운 객체 생성해 리턴
                return new Encoder(urlEncoder);
            }

        }
        ```

- 정리

    - 일반적인 spring 코딩
        - 코딩을 할 때에는 실질적으로 new를 사용해 직접 객체를 생성하지 않음
        - 서비스 로직에서는 항상 spring context를 통해서 가져와야 함
            - 실제로는 `생성자` 또는 `set 메서드` 또는 `변수`에다가 autowired, inject같은 어노테이션을 통해서 직접 객체를 받아옴

    - Bean을 가져오는 두 가지 방법
        1. 클래스 타입으로 가져오기
        2. Bean 이름으로 가져오기

    - 용어 정리
        - 이처럼 Spring에서 직접 관리하는 객체를 `Bean`이라고 함
        - 이러한 Bean들이 관리되고 있는 장소가 `Spring Container`임
        - Spring Container가 객체를 제어하는 권한을 모두 가져갔기 때문에 `제어의 역전(IoC)`이 발생

    - 요약
        - Spring Container가 Bean(객체)을 관리하는 것이 `IoC(Inversion of Container)`이고 개발자는 그러한 Bean(객체)를 주입받아 사용하기 때문에 `DI(Dependency Injection)`임
        - Ioc와 DI는 Spring의 핵심 기술 중 하나

    