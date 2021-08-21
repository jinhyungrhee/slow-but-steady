# PUT Method

- PUT

    - 리소스 갱신, 생성
        - 리소스가 없으면 생성(CREATE), 있으면 갱신(UPDATE)
    - 멱등성 O
        - 처음 한 번은 데이터 생성되고 그 다음부터 계속 업데이트 되기 때문에 데이터는 항상 하나임!(항상 같은 상태 유지)
    - 안정성 X
        - 잘못된 데이터가 전송되더라도 Update 시킴
    - Path Variable 사용
    - Query Parameter를 설정할 수 있지만 일반적으로는 사용 X
        - 생성된 data를 전달받기 때문에 따로 조회할 필요 X (조회는 GET Method)
        - 조회, 리스트의 범위지정, sorting 방법들을 보낼 일이 없음!
    - Data Body에 data를 실어서 보냄
        - 굳이 Query Parameter로 다른 데이터를 보낼 필요 없음
    - POST와 큰 차이 없음

- JSON 디자인
    - PUT : 사용자가 자동차 리스트를 업데이트하거나 새로운 자동차를 등록하는 API. 여러개의 자동차를 보낼 수 있음!
    ```js
    {
        "name" : "stever",
        "age" : 20,
        "car_list" : [
            {
                "name" : "BMW",
                "car_number" : "11가 1234"
            },
            {
                "name" : "A4",
                "car_number" : "22가 3456"
            }
        ]
    }
    ```

- PUT Request 받기
    - car_list가 제대로 들어오지 않았음!
    - `PostRequestDto{name='stever', age=20, carList=null}`
        - PostRequestDto에는 CamelCase로 정의되어 있지만, request JSON에서 snake_case로 보냈기 때문!!  
    

- CamelCase로 된 것을 snake_case로 바꾸는 두 가지 방법
1. class에 대해서 전체적으로 같은 룰을 적용시키는 것 : **@JsonNaming**
    - `@JsonNaming(value = PropertyNamingStrategy.SnakeCaseStrategy.class)`
        - 해당 클래스는 object mapper라는 모듈이 동작할 때 snake_case로 인식함!
        - 폐기될 예정(deprecated)?
    - 결과 
        - `PostRequestDto{name='stever', age=20, carList=[CarDto{name='BMW', carNumber='null'}, CarDto{name='A4', carNumber='null'}]}`
        - carNumber가 null인 이유는 동일함!
        - CarDto에 @JsonNaming이 적용되지 않고 camelCase로만 선언되어 있기 때문
2. 특정 변수만 바꿔주는 것 : **@JsonProperty**  
    ```java
    @JsonProperty("car_number")
    private String carNumber;
    ```
    - 결과
        - `PostRequestDto{name='stever', age=20, carList=[CarDto{name='BMW', carNumber='11가 1234'}, CarDto{name='A4', carNumber='22가 3456'}]}`


- PUT Response 내려주기
    - **RestController인 경우에는 object 자체를 리턴시키면 spring boot 자체에서 해당 object를 가지고 object mapper를 통해서 JSON으로 바꿔줌!** (중요)    
    ```java
    @RestController
    @RequestMapping("/api")
    public class PutApiController {

        // 사용자가 자동차 리스트를 업데이트 하는 API(PUT). 여러 개의 자동차를 보낼 수 있음
        @PutMapping("/put")
        public PostRequestDto put(@RequestBody PostRequestDto requestDto) {
            System.out.println(requestDto);
            return requestDto;
        }
    }
    ```
    - 에코처럼 동작 : 내가 받았던 데이터를 그대로 리턴  


- PUT과 관련된 annotation

    |어노테이션|설명|
    |--|--|
    |@RestController|Rest API 설정|
    |@RequestMapping|리소스를 설정(method로 구분가능)|
    |@PutMapping|Put Resource 설정|
    |@RequestBody|Request Body 부분 Parsing|
    |@PathVariable|URL Path Variable Parsing|

- 정리
    - 가장 첫번째로 해야 하는 것은 **데이터 클래스 디자인**!
        - 내가 어떠한 변수로 받을 것인지, 어떠한 값을 내려줄 것이지 설계

- 코드 정리

    - PutApiController.java
    ```java
    @RestController
    @RequestMapping("/api")
    public class PutApiController {

        // 사용자가 자동차 리스트를 업데이트 하는 API(PUT). 여러 개의 자동차를 보낼 수 있음
        @PutMapping("/put/{userId}")
        public PostRequestDto put(@RequestBody PostRequestDto requestDto, @PathVariable(name="userId") Long id) {
            System.out.println(id);
            return requestDto;
        }

    }
    ```

    - PostRequestDto.java
    ```java
    @JsonNaming(value = PropertyNamingStrategy.SnakeCaseStrategy.class)
    public class PostRequestDto {

        private String name;
        private int age;

        // 사용자가 가진 자동차 등록시키기 - car dto 필요
        // getter 와 setter 설정했으므로 car objet 받기 가능?
        // 리스트 형태로 받기
        private List<CarDto> carList;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public List<CarDto> getCarList() {
            return carList;
        }

        public void setCarList(List<CarDto> carList) {
            this.carList = carList;
        }

        // toString 매서드 오버라이딩

        @Override
        public String toString() {
            return "PostRequestDto{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    ", carList=" + carList +
                    '}';
        }
    }

    ```

    - CarDto.java
    ```java
    public class CarDto {

        private String name;
        @JsonProperty("car_number")
        private String carNumber;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getCarNumber() {
            return carNumber;
        }

        public void setCarNumber(String carNumber) {
            this.carNumber = carNumber;
        }

        // toString 메서드 오버라이딩

        @Override
        public String toString() {
            return "CarDto{" +
                    "name='" + name + '\'' +
                    ", carNumber='" + carNumber + '\'' +
                    '}';
        }
    }
    ```