# JUnit

## 용어

- TDD
    - Test-driven Development
    - 테스트 주도 개발에서 주로 사용
    - 코드의 유지 보수 및 운영 환경에서의 에러를 미리 방지하기 위해서 단위 별로 검증하는 테스트 프레임워크


- 단위테스트
    - 작성한 코드가 기대하는 대로 동작을 하는지 검증하는 절차

- JUnit
    - Java 기반의 단위 테스트를 위한 프레임워크
    - Annotation 기반으로 테스트를 지원하며, Assert를 통하여 **(예상값, 실제값)**를 통해 검증

## 순수 Java에서의 테스트 - 계산기 만들기

1. Gradle java 프로젝트 생성
- build.gradle에 default 확인
    - dependencies - junit-jupiter
    - test - useJUnitPlatform (테스트 코드 작성 가능)
    ```java
    dependencies {
        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'
        testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'
    }

    test {
        useJUnitPlatform()
    }
    ```

2. 인터페이스 생성
- ICalculator.java
    ```java
    public interface ICalculator {
        // 간단하게 더하기 빼기만 구현
        int sum(int x, int y);
        int minus(int x, int y);
    }
    ```

3. 계산기 껍데기(클래스) 생성
- Calculator.java
    ```java
    public class Calculator {
        //계산기 껍데기 생성
        private ICalculator iCalculator;

        // 외부에서 주입받기
        public Calculator(ICalculator iCalculator){
            this.iCalculator = iCalculator;
        }

        public int sum(int x, int y){
            return this.iCalculator.sum(x, y);
        }
        public int minus(int x, int y){
            return this.iCalculator.minus(x, y);
        }
    }
    ```

4. 계산기 구현체 생성 - 원화 계산기
- KrwCalculator.java
    - 껍데기 클래스(ICalculator) 상속 받아서 사용
    ```
    public class KrwCalculator implements ICalculator{

        private int price = 1;

        @Override
        public int sum(int x, int y) {
            x *= price;
            y *= price;
            return x + y;
        }

        @Override
        public int minus(int x, int y) {
            x *= price;
            y *= price;
            return x - y;
        }
    }
    ```

5. 메인에서 활용
- Main.java
```java
public class Main {

    public static void main(String arg[]){
        System.out.println("hello JUnit");

        // krwCalculator 주입해서 사용
        Calculator calculator = new Calculator(new KrwCalculator());

        System.out.println(calculator.sum(10, 10));
    }
}
```

5. 계산기 구현체 추가 - 달러 계산기
- DollarCalculator
```java
public class DollarCalculator implements ICalculator{

    private int price = 1;

    // 달러의 시세 가치 가져오기 - connect() 통해 값 가져오기
    public void init(){
        // naver
        // kakao
        this.price = connect();
    }

    // 특정한 곳에 연결 (통신)
    public int connect(){
        // naver
        // kakao
        return 1100;
    }


    @Override
    public int sum(int x, int y) {
        return 0;
    }

    @Override
    public int minus(int x, int y) {
        return 0;
    }
}
```

6. 계산기는 계산만 해야 하므로 connect()기능은 분리시킴
- MarketApi
    ```java
    public class MarketApi {
        
        // 여러가지 인터넷이 있을 수 있으므로 interface화 가능하지만 일단은 보류
        public int connect(){
            return 1100;
        }
    }
    ```
- 변경된 DollarCalculator
    ```java
    public class DollarCalculator implements ICalculator{

        private int price = 1;
        private MarketApi marketApi;
        
        // MarketApi 주입받아 사용
        public DollarCalculator(MarketApi marketApi){
            this.marketApi = marketApi;
        }

        // connect()를 통해 시세 가져옴
        public void init(){
            this.price = marketApi.connect();
        }

        @Override
        public int sum(int x, int y) {
            return 0;
        }

        @Override
        public int minus(int x, int y) {
            return 0;
        }
    }
    ```

7. Main에서 테스트
- Main.java
    ```java
    public class Main {

        public static void main(String arg[]){
            System.out.println("hello JUnit");
            // marketApi 생성
            MarketApi marketApi = new MarketApi();
            DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
            dollarCalculator.init();

            // dollarCalculator 주입해서 사용
            Calculator calculator = new Calculator(dollarCalculator);

            System.out.println(calculator.sum(10, 10));
        }
    }
    ```

- 잘못된 결과
    ```
    > Task :Main.main()
    hello JUnit
    0
    ```

- 클래스 이곳저곳 타고 들어가면서 원인 찾아보니
    - DollarCalculator의 sum() 리턴값이 0이었음
    ```java
    public class DollarCalculator implements ICalculator{

        private int price = 1;
        private MarketApi marketApi;
        
        // MarketApi 주입받아 사용
        public DollarCalculator(MarketApi marketApi){
            this.marketApi = marketApi;
        }

        // connect()를 통해 시세 가져옴
        public void init(){
            this.price = marketApi.connect();
        }

        @Override
        public int sum(int x, int y) {
            return 0;
        }

        @Override
        public int minus(int x, int y) {
            return 0;
        }
    }
    ```  
    ➡ 이런식으로 Main에서 테스트하고 오류 찾으면 안됨!

## 제대로 JUnit으로 Test해보기

1. test/java 아래 DollarCalculatorTest 클래스 생성
    ```java
    public class DollarCalculatorTest {

        // 테스트용
        @Test
        public void testHello(){
            System.out.println("hello");
        }

        // dollarCalculator 테스트
        @Test
        public void dollarTest(){
            // main에 있던 test 코드 전부 옮김
            // marketApi 생성
            MarketApi marketApi = new MarketApi();
            DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
            dollarCalculator.init();

            // dollarCalculator 주입해서 사용
            Calculator calculator = new Calculator(dollarCalculator);

            System.out.println(calculator.sum(10, 10));

            // (내가 기대하는 값 22000, 함수호출)
            Assertions.assertEquals(22000, calculator.sum(10, 10));
        }
    }
    ```
    - 실행 결과
        ```
        expected: <22000> but was: <0>
        Expected :22000
        Actual   :0
        <Click to see difference>
        ```

2. DollarCalculator 수정

- DollarCalculator.java
    ```java
    public class DollarCalculator implements ICalculator{

        private int price = 1;
        private MarketApi marketApi;
        
        // MarketApi 주입받아 사용
        public DollarCalculator(MarketApi marketApi){
            this.marketApi = marketApi;
        }

        // connect()를 통해 시세 가져옴
        public void init(){
            this.price = marketApi.connect();
        }

        @Override
        public int sum(int x, int y) {
            x *= price;
            y *= price;
            return x + y;
        }

        @Override
        public int minus(int x, int y) {
            x *= price;
            y *= price;
            return x - y;
        }
    }
    ```

3. 다시 테스트한 결과
    ```
    > Task :test
    22000
    hello
    BUILD SUCCESSFUL in 8s
    ```

## 한 단계 더 나아가기 - Mocking

- MarketApi은 항상 1100원이 아님
    - 그때 그때마다 다른 값임
    - 지금은 서버에 연결되지 않아서 고정된 값임

- 과연 1100원이 아닌 다른 값에서도 제대로 동작을 할까?
    - **mocking 처리 사용**

- **mocking**이란?
    - 특정한 객체가 어떤 메서드로 호출이 되었을 때 원하는 결과값을 리턴시켜주는 것

1. Maven repository에서 Mockito 가져오기
    - Mockito Core
    - Mockito JUnit Jupiter
    - build.gradle
        ```java
        dependencies {
            testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'
            testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'
            testImplementation group: 'org.mockito', name: 'mockito-core', version: '3.9.0'
            testImplementation group: 'org.mockito', name: 'mockito-junit-jupiter', version: '3.9.0'
        }
        ```

2. DollarCalculatorTest 클래스에 `@ExtendWith(MockitoExtension.class)` 걸어줌
    - mocking을 할 수 있는 환경 만들어짐

3. MarketApi Mocking 처리

- DollarCalculatorTest.java
    - marketApi를 mocking처리 함으로써 그곳에 들어있는 1100이 리턴되는 것이 아닌 새로 mocking처리한 3000이 리턴되도록 함
    ```java
    @ExtendWith(MockitoExtension.class)
    public class DollarCalculatorTest {

        // market Api mocking 처리
        @Mock
        public MarketApi marketApi;

        // 테스트가 실행되기 이전에
        @BeforeEach
        public void init() {
            // marketApi의 connect()가 호출될 때 3000원을 리턴시킴
            Mockito.lenient().when(marketApi.connect()).thenReturn(3000);
        }

        @Test
        public void testHello(){
            System.out.println("hello");
        }

        @Test
        public void dollarTest(){

            MarketApi marketApi = new MarketApi();
            DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
            dollarCalculator.init();

            Calculator calculator = new Calculator(dollarCalculator);

            Assertions.assertEquals(22000, calculator.sum(10, 10));
            Assertions.assertEquals(0, calculator.minus(10, 10));
        }

        @Test
        public void mockTest(){
            // 위에서 mocking처리된 marketApi 주입받음
            DollarCalculator dollarCalculator = new DollarCalculator(marketApi);
            dollarCalculator.init();

            // dollarCalculator 주입해서 사용
            Calculator calculator = new Calculator(dollarCalculator);

            System.out.println(calculator.sum(10, 10));

            Assertions.assertEquals(60000, calculator.sum(10, 10));
            Assertions.assertEquals(0, calculator.minus(10, 10));
        }
    }
    ```

4. 출력 결과
    - Test 성공
    - 60000원 출력됨
    ```
    > Task :test
    9월 17, 2021 5:39:41 오후 org.junit.platform.launcher.core.EngineDiscoveryOrchestrator lambda$logTestDescriptorExclusionReasons$7
    INFO: 0 containers and 2 tests were Method or class mismatch
    60000
    BUILD SUCCESSFUL in 2s
    ```


## 정리
- 이처럼 따로 Test들을 만들어 Mocking을 사용하여 테스트를 진행하면 기존의 만들었던 내 코드를 변경하지 않아도 되고 내가 추가한 코드도 원래 코드에 영향이 없음!
- Spring에서도 JUnit을 사용하여 코드 테스트와 Mocking처리를 함
    - 네이버API나 Database 연결 등 사용 시 실제로 local 환경에서 붙일 수 없을 때, 굳이 이것들을 호출하지 않아도 "~한 응답을 줄거야"라고 미리 정의한 뒤 메서드들을 테스트할 수 있음 (= 단위 테스트)