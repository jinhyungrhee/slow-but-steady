# Strategy Pattern

- Strategy 패턴

    - 전략 패턴. 객체 지향의 꽃
    - 유사한 행위들을 **캡슐화**하여, 객체의 행위를 바꾸고 싶은 경우 직접 변경하는 것이 아니라 전략만 변경하여 유연하게 확장
    - 개방폐쇄 원칙(OCP)과 의존역전 원칙(DIP) 따름 
    - 특정한 텍스트에 대해서 변화를 주고자 할 때 전략(노말, 베이스64, 암호화 등)을 수정해줌으로써 동일한 결과를 얻을 수 있음
    - **반드시 필요한 3가지**
        1. 전략 메서드를 가진 전략 객체 (Normal Strategy, Base64 Strategy)
        2. 전략 객체를 사용하는 컨텍스트 (Encoder)
        3. 전략 객체를 생성해 컨텍스트에 주입하는 클라이언트 (Main method)

- 코드 예제

    - 전략 객체1 : Normal (NormalStrategy.java)
    ```java
    public class NormalStrategy implements EncodingStrategy{
        @Override
        public String encode(String text) {
            return text;
        }
    }
    ```

    - 전략 객체2 : Base64 (Base64Strategy.java)
    ```java
    import java.util.Base64;
    // 전략2
    public class Base64Strategy implements EncodingStrategy{
        @Override
        public String encode(String text) {
            return Base64.getEncoder().encodeToString(text.getBytes());
        }
    }
    ```

    - 전략 객체3 : append (AppendStrategy.java)
    ```java
    public class AppendStrategy implements EncodingStrategy{
        @Override
        public String encode(String text) {
            return "ABCD"+text;
        }
    }
    ```

    - 전략 객체를 사용하는 컨텍스트 : Encoder (Encoder.java)
    ```java
    // 전략을 주입받아 사용하는 인코더
    public class Encoder {

        private EncodingStrategy encodingStrategy;

        public String getMessage(String message){
            return this.encodingStrategy.encode(message);
        }

        public void setEncodingStrategy(EncodingStrategy encodingStrategy) {
            this.encodingStrategy = encodingStrategy;
        }


    }
    ```

    - 전략 객체를 생성해 컨텍스트에 주입하는 클라이언트(Main.java)
    ```java
    public class Main {

        public static void main(String[] args) {
            Encoder encoder = new Encoder();

            // base64
            EncodingStrategy base64 = new Base64Strategy();

            // normal
            EncodingStrategy normal = new NormalStrategy();

            String message = "hello java";
            
            //전략만 수정
            
            //base64 전략
            encoder.setEncodingStrategy(base64);
            String base64Result = encoder.getMessage(message);
            System.out.println(base64Result); // aGVsbG8gamF2YQ==

            //normal 전략
            encoder.setEncodingStrategy(normal);
            String normalResult = encoder.getMessage(message);
            System.out.println(normalResult); // hello java

            //append 전략
            encoder.setEncodingStrategy(new AppendStrategy());
            String appendResult = encoder.getMessage(message);
            System.out.println(appendResult); // ABCDhello java

        }
    }
    ```