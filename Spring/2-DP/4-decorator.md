# Decorator Pattern

- Decorator 패턴

    - 기존 뼈대(클래스)는 유지하되, 이후 필요한 형태로 꾸밀 때 사용
        - 기본 뼈대는 건드리지 않고 부가적인 첨가를 하면서 속성을 변화시키는 것
    - 확장이 필요한 경우 상속의 대안으로 활용
    - 개방폐쇄 원칙(OCP)과 의존역전 원칙(DIP)를 따름
    - ex) 에스프레소 + 물 -> 아메리카노 / 에스프레소 + 우유 -> 카페라떼...

- 코드 예제

    - 자동차 인터페이스 생성(ICar.java)
    ```java
    public interface ICar {
        // 가격을 리턴하는 메서드
        int getPrice();

        // 가격을 보여주는 메서드
        void showPrice();

    }
    ```

    - Audi 클래스 생성(Audi.java)
        - ICar 인터페이스를 상속받아서 사용
    ```java
    public class Audi implements ICar{

        // 가격
        private int price;

        // default 생성자에서 금액 받음
        public Audi(int price){
            this.price = price;
        }

        @Override
        public int getPrice() {
            return price;
        }

        @Override
        public void showPrice() {
            System.out.println("Audi의 가격은 "+this.price + "원 입니다.");
        }
    }
    ```

    - 데코레이터 생성(AudiDecorator.java)
        - 데코레이터 클래스도 ICar를 상속받음
    ```java
    public class AudiDecorator implements ICar{
    
        // Audi를 받음
        protected ICar audi;
        // 모델 네임을 받음
        protected String modelName;
        // 모델 가격 받음
        protected int modelPrice;

        // default 생성자에서 세 가지 모두 받음
        public AudiDecorator(ICar audi, String modelName, int modelPrice) {
            this.audi = audi;
            this.modelName = modelName;
            this.modelPrice = modelPrice;
        }

        @Override
        public int getPrice() {
            // decorate를 이용하여 등급이 올라갈 때마다 가격이 첨부되도록 설계
            // 기본 audi모델 가격 + 등급별 가격
            return audi.getPrice() + modelPrice;
        }

        @Override
        public void showPrice() {
            System.out.println(modelName+"의 가격은 "+ getPrice()+"원 입니다.");
        }
    }
    ```

    - A3 모델 클래스 생성(A3.java)
    ```java
    // A3는 AudiDecorator를 상속받음
    public class A3 extends AudiDecorator{
        // modelPrice는 받지 않고 직접 정의함!
        public A3(ICar audi, String modelName) {
            super(audi, modelName, 1000);
        }
    }
    ```

    - A4 모델 클래스 생성(A3.java)
    ```java
    // A4는 AudiDecorator를 상속받음
    public class A4 extends AudiDecorator{
        // modelPrice는 받지 않고 직접 정의함!
        public A4(ICar audi, String modelName) {
            super(audi, modelName, 2000);
        }
    }
    ```

    - A5 모델 클래스 생성(A3.java)
    ```java
    // A5는 AudiDecorator를 상속받음
    public class A5 extends AudiDecorator{
        // modelPrice는 받지 않고 직접 정의함!
        public A5(ICar audi, String modelName) {
            super(audi, modelName, 3000);
        }
    }
    ```

    - Main.java
    ```java
    public class Main {

        public static void main(String[] args) {
            ICar audi = new Audi(1000); // 기본 베이스 audi
            audi.showPrice();

            // 기본 베이스 audi를 넘겨서 a3, a4, a5가 첨가된 내용이 나오는지 확인!
            // a3
            ICar audi3 = new A3(audi, "A3");
            audi3.showPrice();

            // a4
            ICar audi4 = new A4(audi, "A4");
            audi4.showPrice();

            // a5
            ICar audi5 = new A5(audi, "A5");
            audi5.showPrice();

        }
    }
    ```