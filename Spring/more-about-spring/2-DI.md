# IoC/DI

## IoC (Inversion of Control)

- 제어의 역전
    - Spring에서는 일반적인 Java 객체를 개발자가 직접 new로 생성하여 사용하는 경우는 거의 없음!
    - Spring Container라는 공간에 생성하고자 하는 객체들이 이미 만들어져서 들어가 있고 Singleton 형태로 관리가 됨
    - **개발자가 객체를 관리하는 것이 아니라 프레임워크에게 제어의 권한을 넘기는 것(제어의 역전)**
        - 모든 객체의 관리를 Spring Container에서 관리함
        - Spring이 알아서 객체의 생명주기를 관리해줌
            - 개발자는 객체를 사용하기 위해 Spring Container로부터 사용할 객체를 **주입(Injection)받음**

## DI(Dependency Injection)

- DI의 장점 (DI를 왜 쓰는가?)

    - 의존성으로부터 격리시켜 코드 테스트에 용이함
    - DI를 통해, 불가능한 상황을 Mocking 같은 기술을 사용하여 안정적으로 테스트할 수 있음
        - 실제로 배포를 하지 않으면 테스트가 불가능한 상황(ex, 통신)에서도 특정한 기대값을 넣어 내 로직이 올바르게 동작하는지 확인할 수 있음
    - 코드를 확장하거나 변경할 때 영향을 최소화함(추상화)
        - 특정 코드가 변경되더라도 나의 내부적인 코드는 안정적으로 대응 가능
    - 순환참조(내가 나를 참조 혹은 내가 참조한 객체가 나를 다시 참조)를 막을 수 있음


## 코드로 알아보기

- Base 64 인코딩과 Url 인코딩 둘 다 해야 하는 경우

- 무지성 코딩 (일일이 생성)

    - Main.java
        ```java
        public class Main {

            public static void main(String[] args) {
                String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                // Base 64 encoding

                Base64Encoder encoder = new Base64Encoder();
                String result = encoder.encode(url);

                // url encoding

                UrlEncoder urlEncoder = new UrlEncoder();
                String urlResult = urlEncoder.encode(url);

                System.out.println(urlResult);
            }
        }
        ```

    - Base64Encoder.java (Base64 인코더 클래스)
        ```java
        import java.nio.charset.StandardCharsets;
        import java.util.Base64;

        public class Base64Encoder {

            public String encode(String message) {
                return Base64.getEncoder().encodeToString(message.getBytes());

            }
        }
        ```

    - UrlEncoder.java (url 인코더 클래스)
        ```java
        import java.io.UnsupportedEncodingException;
        import java.net.URLEncoder;

        public class UrlEncoder {

            public String encode(String message){
                try {
                    return URLEncoder.encode(message, "UTF-8");
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                    return null;
                }
            }
        }
        ```

- 추상화하여 분리

    - UrlEncoder와 Encoder는 서로 동일한 역할을 수행함
        - Encoder라는 Interface 뽑아낼 수 있음!
    
    - IEncoder.java (인코더 인터페이스)
        ```java
        public interface IEncoder {
            // encode라는 메서드 하나 정의
            String encode(String message);
        }
        ```

    - Base64Encoder.java (IEncoder 인터페이스 상속)
        ```java
        public class Base64Encoder implements IEncoder {

            // 인터페이스 상속받아 자동으로 오버라이딩
            public String encode(String message) {
                return Base64.getEncoder().encodeToString(message.getBytes());

            }
        }
        ```

    - UrlEncoder.java (IEncoder 인터페이스 상속)
        ```java
        public class UrlEncoder implements IEncoder {
        
            // 인터페이스 상속받아 자동으로 오버라이딩
            public String encode(String message){
                try {
                    return URLEncoder.encode(message, "UTF-8");
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                    return null;
                }
            }

        }
        ```

    - Main.java
        ```java
        public class Main {

            public static void main(String[] args) {
                String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                // Base 64 encoding

                //Base64Encoder encoder = new Base64Encoder();
                IEncoder encoder = new Base64Encoder();
                String result = encoder.encode(url);

                // url encoding

                //UrlEncoder urlEncoder = new UrlEncoder();
                IEncoder urlEncoder = new UrlEncoder();
                String urlResult = urlEncoder.encode(url);

                System.out.println(urlResult);
            }
        }
        ```

- 클래스 안에 감추기

    - Base64 인코더 사용하기

        - IEncoder.java (인터페이스)
            ```java
            public interface IEncoder {
                // encode라는 메서드 하나 정의
                String encode(String message);
            }
            ```

        - Encoder.java (인코더 클래스)
            ```java
            import java.util.Base64;

                public class Encoder {

                    // 본인이 직접 인코더 인터페이스를 가지고 있다가
                    private IEncoder iEncoder;

                    // 생성자에서 인코더 종류 적용
                    public Encoder() {
                        // 처음에는 Base64 인코더 사용
                        this.iEncoder = new Base64Encoder();
                    }

                    
                    public String encode(String message) {
                        // iEncoder를 통해 encode 호출 - Base64 인코더로 바뀜
                        return iEncoder.encode(message);

                    }
            }
            ```

        - Main.java
            ```java
            public class Main {

                public static void main(String[] args) {
                    String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                    // 확실히 코드가 간결해짐 
                    // Base64 적용하는 과정 Encoder 클래스 안에 숨김
                    Encoder encoder = new Encoder();
                    String result = encoder.encode(url);

                    System.out.println(result);
                }
            }
            ```

        - 결과
            ```
            d3d3Lm5hdmVyLmNvbS9ib29rcy9pdD9wYWdlPTEwJnNpemU9MjAmbmFtZT1zcHJpbmctYm9vdA==
            ```

    - URL 인코더 사용하기

        - IEncoder.java (인터페이스)

            ```java
            public interface IEncoder {
                // encode라는 메서드 하나 정의
                String encode(String message);
            }
            ```

        - Encoder.java (인코더 클래스)

            ```java
            import java.util.Base64;

                public class Encoder {

                    // 본인이 직접 인코더 인터페이스를 가지고 있다가
                    private IEncoder iEncoder;

                    // 생성자에서 인코더 종류 적용
                    public Encoder() {
                        // 처음에는 Base64 인코더 사용
                        // this.iEncoder = new Base64Encoder();
                        
                        // 이후에 Url 인코더로 사용
                        this.iEncoder = new UrlEncoder();
                    }

                    
                    public String encode(String message) {
                        // iEncoder를 통해 encode 호출 - Base64 인코더로 바뀜
                        return iEncoder.encode(message);

                    }
            }
            ```

        - Main.java

            ```java
            public class Main {

                public static void main(String[] args) {
                    String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                    // 확실히 코드가 간결해짐 
                    // Base64 적용하는 과정 Encoder 클래스 안에 숨김
                    Encoder encoder = new Encoder();
                    String result = encoder.encode(url);

                    System.out.println(result);
                }
            }
            ```

        - 결과
            ```
            www.naver.com%2Fbooks%2Fit%3Fpage%3D10%26size%3D20%26name%3Dspring-boot
            ```

        - 정리
            - 굉장히 비효율적(필요할 때마다 직접 클래스 안의 내용을 변경)이고 본질(클래스)을 건드리고 있음!
            - **DI** 개념을 도입하면 본질을 건드리지 않고도 재활용이나 테스트가 가능함!!
                - `DI` : 외부에서 내가 사용하는 객체를 주입시켜 주는 것

- DI 적용하기

    - 생성자에서 인터페이스 받아야 함!

        - Encoder.java (Encoder 클래스)
            - Encoder의 입장에서는  IEncoder를 외부에서 주입받은 것
            - 의존을 가지고 있는 것을 주입받은 것 (Dependency Injection)

        ```java
        public class Encoder {

                private IEncoder iEncoder;

                // DI : 생성자에서 인터페이스를 주입받아서 사용
                public Encoder(IEncoder iEncoder) {
                    this.iEncoder = iEncoder;
                }

                
                public String encode(String message) {
                    // iEncoder를 통해 encode 호출
                    return iEncoder.encode(message);

                }
        }
        ```

        - Main.java

        ```java
        public class Main {

            public static void main(String[] args) {
                String url = "www.naver.com/books/it?page=10&size=20&name=spring-boot";

                // DI : main에서 주입해서 사용
                // Encoder 클래스를 수정하지 않아도 Base64/Url 인코더로 작동
                // 넘겨주는 주입 객체만 변경! (외부에서 사용하는 객체를 주입받는 형태)

                Encoder encoder = new Encoder(new UrlEncoder());
                // Encoder encoder = new Encoder(new Base64Encoder());
                String result = encoder.encode(url);

                System.out.println(result);
            }
        }
        ```