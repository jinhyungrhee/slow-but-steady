# Adapter Pattern

- Adapter 패턴

    - 호환성이 없는 기존 클래스의 인터페이스를 변환하여 재사용할 수 있도록 함
    - SOLID 원칙 중 개방폐쇄 원칙(OCP)를 따름 
    - 자기 자신의 상태는 변환시키지 않고 중간에 인터페이스를 사용하여 조건을 맞춤
    - 인터페이스가 달라서 서로 맞춰지지 않는 상황에서 중간에 어댑터 클래스를 두고 연결시키는 형태

- 코드 예제

    - 110V 인터페이스(Electronic110V.java)
    ```java
    public interface Electronic110V {

        void powerOn();
    }
    ```

    - 220V 인터페이스(Electronic220V.java)
    ```java
    public interface Electronic220V {

        void connect();
    }
    ```
    
    - 110V 헤어드라이기 클래스(HairDryer.java)
    ```java
    public class HairDryer implements Electronic110V {
        @Override
        public void powerOn() {
            System.out.println("헤어 드라이기 110v on");
        }
    }
    ```

    - 220V 청소기 클래스(Cleaner.java)
    ```java
    public class Cleaner implements Electronic220V{
        @Override
        public void connect() {
            System.out.println("청소기 220V on");
        }
    }
    ```

    - 220V 에어컨 클래스(AirConditioner.java)
    ```java
    public class AirConditioner implements Electronic220V{
        @Override
        public void connect() {
            System.out.println("에어컨 220V on");
        }
    }
    ```

    - 110V 어댑터 클래스(SocketAdapter.java) : 220V -> 110V
    ```java
    public class SocketAdapter implements Electronic110V{

        // 자기가 연결시켜줘야 할 220V를 안에 가지고 있어야 함
        private Electronic220V electronic220V;
        
        // 디폴트 생성자에서 electronic220V를 받음
        public SocketAdapter(Electronic220V electronic220V) {
            // 내가 가진 220V 가전제품 할당
            this.electronic220V = electronic220V;
        }
        
        @Override
        public void powerOn() {
            // 110v에 220v가 할당되었을 때 220v의 connect를 호출함
            electronic220V.connect();
        }
    }
    ```

    - Main.java
    ```java
    public class Main {

        public static void main(String[] args) {

            // 1. 헤어 드라이어 생성
            HairDryer hairDryer = new HairDryer();

            // 110V 콘센트에 연결
            connect(hairDryer);


            // 2. 청소기 생성
            Cleaner cleaner = new Cleaner();

            // 110V 콘센트 연결 - cleaner는 220V를 상속받았기 때문에 문제 발생
            //connect(cleaner);
            
            // 110v 변환 adapter 적용
            Electronic110V adapter = new SocketAdapter(cleaner);

            // adapter를 사용하여 110v 콘센트에 연결
            connect(adapter);


            // 3. 에어컨 생성
            AirConditioner airConditioner = new AirConditioner();

            // 에어컨도 220v이므로 110v 콘센트인 connect에 연결불가
            //connect(airConditioner);

            // adapter를 사용하여 110v 콘센트에 연결
            Electronic110V airAdapter = new SocketAdapter(airConditioner);

            // adapter를 낀 채로 110v 콘센트에 연결
            connect(airAdapter);

        }
        
        // 110v의 콘센트 생성
        public static void connect(Electronic110V electronic110V){
            electronic110V.powerOn();
        }
    }

    ```