# REST API CRUD 테스트 코드

## REST API 코드 작성

1. Spring 프로젝트(spring-calculator)로 진행
    - spring 버전이 올라가면서 junit에서 junit-jupiter로 변경됨
    - 이에 맞춰서 테스트 코드 작성할 것!

2. 이전 예제에서 MarketApi, ICalculator, DollarCalculator, Calculator 그대로 가져옴
    - spring에서는 더 이상 new로 만들어서 사용하지 않음!
    - 모두 component 패키지 하위로 넣어줌
    - DollarCalculator는 spring에 의해서 bean으로 관리되도록 함
        - DollarCalculator 클래스에서 marketApi 주입받아서 사용
        - 따라서 marketApi도 component가 되어야 함!
        ```java
        @Component
        public class DollarCalculator implements ICalculator {

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
        ```java
        @Component
        public class MarketApi {
            
            // 여러가지 인터넷이 있을 수 있으므로 interface화 가능하지만 일단은 보류
            public int connect(){
                return 1100;
            }
        }
        ```
    - Calculator도 Component로 등록
        - ICalculator의 후보군이 DollarCarculator 밖에 없으므로 자동으로 주입됨
            - @Autowired나 자동주입으로 Calculator 자체를 활용할 수 있음
        ```java
        @Component
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

3. controller 생성

- controller/CalculaotorApiController
    ```java
    @RestController
    @RequestMapping("/api")
    @RequiredArgsConstructor
    public class CalculatorApiController {

        // Calculator 받아서 사용할 것
        private final Calculator calculator;

        @GetMapping("/sum")
        public int sum(@RequestParam int x, @RequestParam int y){
            return calculator.sum(x, y);
        }

        @GetMapping("/minus")
        public int minus(@RequestParam int x, @RequestParam int y){
            return calculator.minus(x, y);
        }
    }
    ```

4. 나머지도 spring 형식에 맞게 바꿔줌

- ICalculator.java
    - init()메서드 추가
    ```java
    public interface ICalculator {
        // 간단하게 더하기 빼기만 구현
        int sum(int x, int y);
        int minus(int x, int y);
        void init();
    }
    ```

- Calculator.java
    ```java
    @Component
    @RequiredArgsConstructor
    public class Calculator {
        // spring스럽게 변경
        private final ICalculator iCalculator;

        // 생성자에서 주입받는 코드 더 이상 필요 X
        //public Calculator(ICalculator iCalculator){
        //    this.iCalculator = iCalculator;
        //}

        public int sum(int x, int y){
            // 계산하기 전에 그때 그때 서버로부터 시세 정보를 받아오는 과정
            this.iCalculator.init();
            return this.iCalculator.sum(x, y);
        }
        public int minus(int x, int y){
            // 계산하기 전에 그때 그때 서버로부터 시세 정보를 받아오는 과정
            this.iCalculator.init();
            return this.iCalculator.minus(x, y);
        }
    }
    ```

- DollarCalculator.java
    - 인터페이스에서 추가된 init() 오버라이딩
    ```java
    @Component
    @RequiredArgsConstructor
    public class DollarCalculator implements ICalculator {

        private int price = 1;
        // Spring스럽게 사용
        private final MarketApi marketApi;
        
        // 생성자에서 MarketApi 주입받아 사용 X
        //public DollarCalculator(MarketApi marketApi){
        //    this.marketApi = marketApi;
        // }

        // override 통해 init() 호출
        @Override
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

## 굳이 서버 실행시키지 않고 REST API 테스트하는 방법

- 주의
    - test아래 있는 패키지가 실제 코드의 패키지와 동일해야 함
        - test/java/com.exmple.springcalculator
    - SpringCalculatorApplicationTests가 존재해야 함
        - @SpringBootTest 어노테이션이 있으면 실질적으로 Spring Container가 올라가면서 전체적인 테스트가 가능해지는 것!
            ```java
            @SpringBootTest
            class SpringCalculatorApplicationTests {

                @Test
                void contextLoads() {
                }

            }
            ```
        - 실행시켜보면 실제 spring과 똑같이 동작함
    - 보통 테스트를 실시할 땐 동일한 위치(test/java/com.exmple.springcalculator)에다가 코드 작성해서 테스트 진행!
        - component 패키지 생성
            1. 여기에서 DollarCalculator만 생성해서 테스트하는 것 가능
            2. CalculatorApiController까지 같이 테스트 하는 것 가능
    - JUnit을 사용하는 것은 이전 예제와 동일하고 Spring에서 Bean을 사용한다는 것만 다름!

1. DollarCalculator만 테스트 해보기(통합테스트)

- test 아래 component 디렉토리와 DollarCalculator 클래스 생성

    - component/DollarCalculator.java
        ```java
        //내가 필요한 MarketApi import시킴
        //테스트하고 싶은 DollarCalculatorTest도 함께 받음
        @SpringBootTest
        // @SpringBootTest 붙이는 순간 모든 Bean이 다 import 됨 => 통합테스트 (@Import 없어도 됨!)
        //@Import({MarketApi.class, DollarCalculator.class})
        public class DollarCalculatorTest {

            // spring에서는 bean으로 관리되고 있기 때문에 marketApi를 mocking 처리하기 위해서 @MockBean 사용
            @MockBean
            private MarketApi marketApi;

            // spring이 관리하고 있는 Bean을 @Autowired로 받음
            @Autowired
            private Calculator calculator;

            // DollarController는 바로 테스트
            @Test
            public void dollarCalculatorTest(){
                // marketApi의 connect가 일어날 때 3000을 리턴시키겠다
                Mockito.when(marketApi.connect()).thenReturn(3000);


                int sum = calculator.sum(10, 10);
                int minus = calculator.minus(10, 10);

                Assertions.assertEquals(60000, sum);
                Assertions.assertEquals(0, minus);
            }
        }
        ```

- test 결과
    - 정상적으로 작동


2. Controller에서 단위테스트 실행

- DollorCalculatorTest와 동일한 방식으로 test 아래 controller 디렉토리와 CalculatorApiControllerTest 클래스 생성

- GET 테스트
    - controller/CalculatorApiControllerTest.java
        ```java
        //web으로 CalculatorApiController 클래스만
        @WebMvcTest(CalculatorApiController.class)
        @AutoConfigureWebMvc
        // apiController에서 Calculator 주입받고 있기 때문에 Bean으로 등록해줌
        // calculator는 ICalculator 주입받고 있음
        @Import({Calculator.class, DollarCalculator.class})
        public class CalculatorApiControllerTest {

            // mocking처리
            @MockBean
            private MarketApi marketApi;

            // Mvc를 Mocking으로 테스트하겠다
            @Autowired
            private MockMvc mockMvc;

            // 테스트 사전에 미리 등록
            @BeforeEach
            public void init(){
                Mockito.when(marketApi.connect()).thenReturn(3000);
            }

            @Test
            public void sumTest() throws Exception {
                // http://localhost:8080/api/sum

                mockMvc.perform(
                        MockMvcRequestBuilders.get("http://localhost:8080/api/sum")
                                .queryParam("x", "10")
                                .queryParam("y", "10")
                ).andExpect( // 기대하는 값
                        MockMvcResultMatchers.status().isOk()
                ).andExpect( // 그 다음에 기대하는 값
                        MockMvcResultMatchers.content().string("60000")
                ).andDo(MockMvcResultHandlers.print()); // 내용 출력
            }
        }
        ```

    - test 결과
        - 정상 작동
            ```
            MockHttpServletRequest:
                HTTP Method = GET
                Request URI = /api/sum
                Parameters = {x=[10], y=[10]}
                    Headers = []
                        Body = null
                Session Attrs = {}

            Handler:
                        Type = com.example.springcalculator.controller.CalculatorApiController
                    Method = com.example.springcalculator.controller.CalculatorApiController#sum(int, int)

            Async:
                Async started = false
                Async result = null

            Resolved Exception:
                        Type = null

            ModelAndView:
                    View name = null
                        View = null
                        Model = null

            FlashMap:
                Attributes = null

            MockHttpServletResponse:
                    Status = 200
                Error message = null
                    Headers = [Content-Type:"application/json"]
                Content type = application/json
                        Body = 60000
                Forwarded URL = null
            Redirected URL = null
                    Cookies = []
            BUILD SUCCESSFUL in 7s
            4 actionable tasks: 2 executed, 2 up-to-date
            오전 10:57:07: Task execution finished ':test --tests "com.example.springcalculator.controller.CalculatorApiControllerTest.sumTest"'.
            ```

    - POST 테스트

        - main에서 dto/Req.java와 Res.java 생성 (POST)
            - Req.java
                ```java
                import lombok.AllArgsConstructor;
                import lombok.Data;
                import lombok.NoArgsConstructor;

                @Data
                @AllArgsConstructor
                @NoArgsConstructor
                public class Req {
                    private int x;
                    private int y;
                }
                ```
            - Res.java
                ```java
                @Data
                @AllArgsConstructor
                @NoArgsConstructor
                public class Res {
                    private int result;

                    private Body response;

                    // 조금 복잡하게 JSON에 depth를 둠
                    @Data
                    @AllArgsConstructor
                    @NoArgsConstructor
                    public static class Body{
                        private String resultCode = "OK";
                    }
                }
                ```

        - CalculatorApiController에서 @Postmapping으로 변경
            ```java
            @RestController
            @RequestMapping("/api")
            @RequiredArgsConstructor
            public class CalculatorApiController {

                // Calculator 받아서 사용할 것
                private final Calculator calculator;

                @GetMapping("/sum")
                public int sum(@RequestParam int x, @RequestParam int y){
                    return calculator.sum(x, y);
                }

                @PostMapping("/minus")
                public Res minus(@RequestBody Req req){
                    // 계산기로 계산한 뒤
                    int result = calculator.minus(req.getX(), req.getY());
                    // Response로 내려줌ㄴ
                    Res res = new Res();
                    res.setResult(result);
                    return res;
                }
            }
            ```

        - test/controller/CalculatorApiControllerTest에서 테스트 코드 작성
            ```java
            @WebMvcTest(CalculatorApiController.class)
            @AutoConfigureWebMvc
            @Import({Calculator.class, DollarCalculator.class})
            public class CalculatorApiControllerTest {

                // mocking처리
                @MockBean
                private MarketApi marketApi;

                // Mvc를 Mocking으로 테스트하겠다
                @Autowired
                private MockMvc mockMvc;

                // 테스트 사전에 미리 등록
                @BeforeEach
                public void init(){
                    Mockito.when(marketApi.connect()).thenReturn(3000);
                }

                @Test
                public void sumTest() throws Exception {
                    // http://localhost:8080/api/sum

                    mockMvc.perform(
                            MockMvcRequestBuilders.get("http://localhost:8080/api/sum")
                                    .queryParam("x", "10")
                                    .queryParam("y", "10")
                    ).andExpect( // 기대하는 값
                            MockMvcResultMatchers.status().isOk()
                    ).andExpect( // 그 다음에 기대하는 값
                            MockMvcResultMatchers.content().string("60000")
                    ).andDo(MockMvcResultHandlers.print()); // 내용 출력
                }

                // 내가 만든 controller가 잘 작동하는지 테스트하는 코드
                @Test
                public void minusTest() throws Exception {

                    // request 보내야함
                    Req req = new Req();
                    req.setX(10);
                    req.setY(10);

                    // 순수한 JSON으로 날아가야함 - JSON으로 바꿔주기
                    String json = new ObjectMapper().writeValueAsString(req);

                    // post로 요청
                    mockMvc.perform(
                            MockMvcRequestBuilders.post("http://localhost:8080/api/minus")
                                    .contentType(MediaType.APPLICATION_JSON)
                                    .content(json)
                    ).andExpect(
                            MockMvcResultMatchers.status().isOk()
                    ).andDo(MockMvcResultHandlers.print());
                }
            }
            ```

        - 출력 결과
            - 정상출력되었지만 Body의 "response" 부분에 null값이 들어있음
            ```
            MockHttpServletRequest:
                HTTP Method = POST
                Request URI = /api/minus
                Parameters = {}
                    Headers = [Content-Type:"application/json;charset=UTF-8", Content-Length:"15"]
                        Body = {"x":10,"y":10}
                Session Attrs = {}

            Handler:
                        Type = com.example.springcalculator.controller.CalculatorApiController
                    Method = com.example.springcalculator.controller.CalculatorApiController#minus(Req)

            Async:
                Async started = false
                Async result = null

            Resolved Exception:
                        Type = null

            ModelAndView:
                    View name = null
                        View = null
                        Model = null

            FlashMap:
                Attributes = null

            MockHttpServletResponse:
                    Status = 200
                Error message = null
                    Headers = [Content-Type:"application/json"]
                Content type = application/json
                        Body = {"result":0,"response":null}
                Forwarded URL = null
            Redirected URL = null
                    Cookies = []

            ```

        - Body "response" 의 null값 해결하기
            - main/controller/CalculatorApiController.java
            ```java
            @RestController
            @RequestMapping("/api")
            @RequiredArgsConstructor
            public class CalculatorApiController {

                // Calculator 받아서 사용할 것
                private final Calculator calculator;

                @GetMapping("/sum")
                public int sum(@RequestParam int x, @RequestParam int y){
                    return calculator.sum(x, y);
                }

                @PostMapping("/minus")
                public Res minus(@RequestBody Req req){
                    // 계산기로 계산한 뒤
                    int result = calculator.minus(req.getX(), req.getY());
                    // Response로 내려줌ㄴ
                    Res res = new Res();
                    res.setResult(result);
                    // 추가 - body를 만들어서 response로 넣어줌
                    res.setResponse(new Res.Body());
                    return res;
                }
            }
            ```

        - test/controller/CalculatorApiControllerTest.java
            ```java
            @WebMvcTest(CalculatorApiController.class)
            @AutoConfigureWebMvc
            @Import({Calculator.class, DollarCalculator.class})
            public class CalculatorApiControllerTest {

                // mocking처리
                @MockBean
                private MarketApi marketApi;

                // Mvc를 Mocking으로 테스트하겠다
                @Autowired
                private MockMvc mockMvc;

                // 테스트 사전에 미리 등록
                @BeforeEach
                public void init(){
                    Mockito.when(marketApi.connect()).thenReturn(3000);
                }

                @Test
                public void sumTest() throws Exception {
                    // http://localhost:8080/api/sum

                    mockMvc.perform(
                            MockMvcRequestBuilders.get("http://localhost:8080/api/sum")
                                    .queryParam("x", "10")
                                    .queryParam("y", "10")
                    ).andExpect( // 기대하는 값
                            MockMvcResultMatchers.status().isOk()
                    ).andExpect( // 그 다음에 기대하는 값
                            MockMvcResultMatchers.content().string("60000")
                    ).andDo(MockMvcResultHandlers.print()); // 내용 출력
                }

                // 내가 만든 controller가 잘 작동하는지 테스트하는 코드
                @Test
                public void minusTest() throws Exception {

                    // request 보내야함
                    Req req = new Req();
                    req.setX(10);
                    req.setY(10);

                    // 순수한 JSON으로 날아가야함 - JSON으로 바꿔주기
                    String json = new ObjectMapper().writeValueAsString(req);

                    // post로 요청
                    mockMvc.perform(
                            MockMvcRequestBuilders.post("http://localhost:8080/api/minus")
                                    .contentType(MediaType.APPLICATION_JSON)
                                    .content(json)
                    ).andExpect(
                            MockMvcResultMatchers.status().isOk()
                    ).andExpect(//jsonPath의 값이 내가 기대하는 값과 같은지 확인
                            MockMvcResultMatchers.jsonPath("$.result").value("0")
                    ).andExpect(
                            MockMvcResultMatchers.jsonPath("$.response.resultCode").value("OK")
                    )
                    .andDo(MockMvcResultHandlers.print());
                }
            }
            ```

        - 출력 결과
            ```
            MockHttpServletRequest:
                HTTP Method = POST
                Request URI = /api/minus
                Parameters = {}
                    Headers = [Content-Type:"application/json;charset=UTF-8", Content-Length:"15"]
                        Body = {"x":10,"y":10}
                Session Attrs = {}

            Handler:
                        Type = com.example.springcalculator.controller.CalculatorApiController
                    Method = com.example.springcalculator.controller.CalculatorApiController#minus(Req)

            Async:
                Async started = false
                Async result = null

            Resolved Exception:
                        Type = null

            ModelAndView:
                    View name = null
                        View = null
                        Model = null

            FlashMap:
                Attributes = null

            MockHttpServletResponse:
                    Status = 200
                Error message = null
                    Headers = [Content-Type:"application/json"]
                Content type = application/json
                        Body = {"result":0,"response":{"resultCode":"OK"}}
                Forwarded URL = null
            Redirected URL = null
                    Cookies = []

            ```

## 정리

- 번거롭게 Talend API에 들어가서 test하지 않아도 됨!
- 내가 만든 controller와 service(=component)를 테스트 코드를 작성해서 내가 기대했던대로 잘 동작하는지 확인 가능 (기대값)
    - 다른 팀원이 내 코드를 수정했을 때 기대값을 통해 제대로 수정했는지 확인할 수 있음!
