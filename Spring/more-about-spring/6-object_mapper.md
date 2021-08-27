# Object Mapper 자세히 알아보기

- JSON 노드 자체를 controll 하는 부분을 알아봄
    - 실제 현업 업무에서는 controller를 통해 validation하고 request받는 것이 거의 대부분
    - **하지만 JSON 내부 상태 변경이나 값들을 확인하기 위해서는 JSON 노드에 직접 접근해서 활용할 줄도 알아야 함!**

- Object Mapper 활용하기(**Object Mapper를 통한 JSON 노드 접근**)
    - Java에서 많이 사용하는 JSON 관련 라이브러리
        1. Google Gson
        2. Object Mapper (=> Spring에서 많이 사용)

    - Spring 프로젝트 사용X
        - `Object Mapper`는 Spring 프레임워크에서 사용하는 자바 라이브러리임
        - 따라서 Object Mapper가 꼭 Spring에서만 사용할 수 있는 것은 아님!
        - 실습 예제는 **Java 프로젝트**에서 진행
            - `Gradle dependency`를 사용하기 때문에 Gradle에서 Java 프로젝트 생성(obejct_mapper)
    
    - Gradle dependency를 가진 Java 프로젝트(=> **Gradle 프로젝트**)
        - 이러한 `dependency`들(라이브러리들)은 어디서 찾아 오는가?
            - 일반적으로 Maven으로 설정하지만 우리는 Gradle로 활용하고 있음
            - maven repository에서 검색(https://mvnrepository.com/)
                - 'spring boot' 검색
                    - Spring Boot Starter Test
                    - Spring Boot AutoConfigure
                    - Spring Boot Starter Web 등등
                - 'object mapper' 검색
                    - Data Mapper For Jackson
                    - **Jackson Databind** 등등
            - 어떤 버전을 사용해야 할까? (버전 선택)
                - 지속적으로 버전이 업데이트 되는 프레임워크(라이브러리) 경우, 가장 최신버전보다는 `중간버전` 또는 `RELEASE버전` 주로 사용!
                    - 가장 최신버전의 경우 하위호환성이 없어졌거나 dependency가 변경되었을 수도 있기 때문
                    - 이러한 버전을 가져다 썼을 때 우리 코드의 많은 부분을 변경해야 할 수도 있음
            - 이번 실습에서는 Jackson Databind - com.fasterxml.jackson.core 사용
                - `2.12.1 버전` 클릭 (아마 홀수가 안정된 버전이고 짝수가 불안정한 버전?)
                - Gradle탭 클릭 (우리는 Maven대신 Gradle 활용중)
                - 해당 내용 복사
                    ```
                    // https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind
                    implementation group: 'com.fasterxml.jackson.core', name: 'jackson-databind', version: '2.12.1'
                    ```
                - build.gradle파일의 dependencies에 해당 코드 붙여넣기
                    ```java
                    dependencies {
                        // https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind
                        implementation group: 'com.fasterxml.jackson.core', name: 'jackson-databind', version: '2.12.1'
                        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.7.0'
                        testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.7.0'
                    }
                    ```
                - 새로고침 버튼(코끼리 모양) 클릭
                    - spring boot가 직접 온라인으로 Jackson Databind 라이브러리 가져오고 해당 라이브러리 jar파일을 프로젝트에 추가해줌!
                        - 일반적인 Java 프로젝트에서는 lib 디렉토리 생성 후 그곳에 jar파일을 추가해서 build하는 방식으로 진행
                        - ❗**Gradle 프로젝트나 Maven 프로젝트를 사용하면 단순히 dependency를 추가해주는 것만으로도 spring이 알아서 온라인에서 해당 라이브러리를 찾아 프로젝트에 추가해줌**❗

                - dependency가 추가되었는지 확인하는 방법
                    1. 오른쪽 Gradle 탭의 Dependencies에서 compileClasspath 확인
                        - compile될 때 jackson-databind:2.12.1도 같이 compile되는 것 확인할 수 있음
                        - jackson-databind:2.12.1가 가지고 있는 dependency들도 하위에 같이 표시가 됨
                    2. External Libraries에서 확인  
                <br>
                ➡ **Object Mapper 사용 준비 끝!!**

    1. 클래스 디자인 및 JSON 설계 
        - JSON 설계
            - sample.json
            ```js
            {
            "name":"홍길동",
            "age":10,
            "cars":[
                {
                    "name":"K5",
                    "car_number":"11가 1111",
                    "TYPE":"sedan"
                },
                {
                    "name":"Q5",
                    "car_number":"22가 2222",
                    "TYPE":"SUV"
                }
            ]
            }
            ```

        - 클래스 디자인(dto)
            - dto/User.java
                ```java
                public class User {
                    private String name;
                    private int age;
                    private List<Car> cars;

                    // getter & setter
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

                    public List<Car> getCars() {
                        return cars;
                    }

                    public void setCars(List<Car> cars) {
                        this.cars = cars;
                    }

                    // toStirng 오버라아딩

                    @Override
                    public String toString() {
                        return "User{" +
                                "name='" + name + '\'' +
                                ", age=" + age +
                                ", cars=" + cars +
                                '}';
                    }
                }
                ```
            - dto/Car.java
                ```java
                public class Car {
                    private String name;
                    private String carNumber;
                    private String type;

                    // getter & setter

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

                    public String getType() {
                        return type;
                    }

                    public void setType(String type) {
                        this.type = type;
                    }
                    
                    // toString 오버라이딩
                    @Override
                    public String toString() {
                        return "Car{" +
                                "name='" + name + '\'' +
                                ", carNumber='" + carNumber + '\'' +
                                ", type='" + type + '\'' +
                                '}';
                    }
                }
                ```

    2. Main 클래스 생성
        - Main.java
            ```java
            public class Main {

                public static void main(String args[]){
                    System.out.println("main");
                
                    // object mapper 생성
                    ObjectMapper objectMapper = new ObjectMapper();
                    
                    // object mapper에서 사용할 객체 생성
                    User user = new User();
                    user.setName("홍길동");
                    user.setAge(10);

                    Car car1 = new Car();
                    car1.setName("K5");
                    car1.setCarNumber("11가 1111");
                    car1.setType("sedan");

                    Car car2 = new Car();
                    car2.setName("Q5");
                    car2.setCarNumber("22가 2222");
                    car2.setType("SUV");

                    List<Car> carList = Arrays.asList(car1, car2);
                    user.setCars(carList);

                    System.out.println(user);
                }
            }
            ```
        - Main에서 객체 생성한 뒤에 출력하면 **인코딩 에러 발생**
            - `error: unmappable character (0xEC) for encoding x-windows-949 // toString ?��버라?��?��`
            - 우리가 사용하는 Window 환경에서는 UTF-8이 아닌 MS949 사용 (MAC은 default가 UTF-8)
            - **해결방법**
                - File - Settings - File Encodings
                    - Project Encoding을 UTF-8로 변경 
                    - Default encoding for properties files도 UTF-8로 변경
                - Help - find action - 'edit custom VM Options' 검색
                    - idea64.exe.vmoptions 파일 마지막에 `-Dfile.encoding=UTF-8`추가
                - 실행중인 모든 intellij창 닫고 다시 실행
        
        - 에러 해결 후 출력 결과
            - 정상 출력
            ```shell
            > Task :Main.main()
            main
            User{name='홍길동', age=10, cars=[Car{name='K5', carNumber='11가 1111', type='sedan'}, Car{name='Q5', carNumber='22가 2222', type='SUV'}]}
            ```

        - ❗주의❗
            - **윈도우 환경**의 자바 프로젝트에서 JSON 데이터를 만들어서 보내야 하거나 순수 자바 Util에 있는 것을 통해 HTTP 통신을 할 때는 **반드시 인코딩을 UTF-8**로 해주어야 함!
                - JSON default encoding : UTF-8
                - Windows default encoding : MS949
        
        - 빌드 시 Deprecated Gradle features were used in this build, making it incompatible with Gradle 8.0.에러 발생 (미해결)
            - Gradle 버전이 올라가면서 같이 프로젝트의 Gradle 버전을 올려줘야 하는데 안 올려줘서 생기는 에러 (무시 가능)
            - 해결방법
                1. 빌드 시 옵션을 줘서 해당 기능을 끔
                2. 그래들 버전을 올림

    3. Object Mapper의 기본적인 사용 🌟
        - Object JSON을 String JSON으로 변환하여 출력
        - Main.java
            ```java
            public class Main {

                public static void main(String args[]) throws JsonProcessingException {
                    System.out.println("main");
                
                    // object mapper 생성
                    ObjectMapper objectMapper = new ObjectMapper();
                    
                    // object mapper에서 사용할 객체 생성
                    User user = new User();
                    user.setName("홍길동");
                    user.setAge(10);

                    Car car1 = new Car();
                    car1.setName("K5");
                    car1.setCarNumber("11가 1111");
                    car1.setType("sedan");

                    Car car2 = new Car();
                    car2.setName("Q5");
                    car2.setCarNumber("22가 2222");
                    car2.setType("SUV");

                    List<Car> carList = Arrays.asList(car1, car2);
                    user.setCars(carList);

                    //System.out.println(user);

                    // object mapper 사용 : Object JSON를 String JSON으로 변환
                    // 에러 발생 가능성 - throw 처리
                    String json = objectMapper.writeValueAsString(user);
                    System.out.println(json);
                }
            }
            ```
        
        - 출력 결과
            - console
            ```shell
            > Task :Main.main()
            main
            {"name":"홍길동","age":10,"cars":[{"name":"K5","carNumber":"11가 1111","type":"sedan"},{"name":"Q5","carNumber":"22가 2222","type":"SUV"}]}
            ```

            - 결과값이 너무 길면 파악이 어려우므로 json validator 사용하여 확인
                - https://jsonformatter.curiousconcept.com/
                - Formatted JSON Data
                    ```js
                    {
                        "name":"홍길동",
                        "age":10,
                        "cars":[
                            {
                                "name":"K5",
                                "carNumber":"11가 1111",
                                "type":"sedan"
                            },
                            {
                                "name":"Q5",
                                "carNumber":"22가 2222",
                                "type":"SUV"
                            }
                        ]
                    }
                    ```

        - 하지만 carNumber가 아직 camelCase로 출력됨
            - snake_case로 맞춰주는 것 필요
            1. 변수에 일일이 붙여주는 방법 : @JsonProperty()
                - 예제에서는 어차피 TYPE이라는 변수가 규격에 위배된 형태로 정해졌기 때문에 @JsonProperty()를 사용하여 일일이 지정
            2. 클래스 전체에 설정하는 방법(통일) : @Json

            - 변경 결과
                ```shell
                > Task :Main.main()
                main
                {"name":"홍길동","age":10,"cars":[{"name":"K5","car_number":"11가 1111","TYPE":"sedan"},{"name":"Q5","car_number":"22가 2222","TYPE":"SUV"}]}
                ```
        ➡ 여기까지는 기본적인 Object Mapper의 방식임

    4. Object Mapper로 순수한 JSON 노드에 접근하기 🌟
        - sample.json이 하나의 노드가 될 수 있음
            - 그 안에 각각의 값들 존재
        - cars 리스트는 새로운 JSON 노드가 됨
            - 정확히는 배열의 노드임
        - Main.java
            ```java
            public class Main {

                public static void main(String args[]) throws JsonProcessingException {
                    System.out.println("main");
                
                    ObjectMapper objectMapper = new ObjectMapper();
                    
                    User user = new User();
                    user.setName("홍길동");
                    user.setAge(10);

                    Car car1 = new Car();
                    car1.setName("K5");
                    car1.setCarNumber("11가 1111");
                    car1.setType("sedan");

                    Car car2 = new Car();
                    car2.setName("Q5");
                    car2.setCarNumber("22가 2222");
                    car2.setType("SUV");

                    List<Car> carList = Arrays.asList(car1, car2);
                    user.setCars(carList);

                    String json = objectMapper.writeValueAsString(user);
                    System.out.println(json);

                    // << JSON 노드에 접근해서 parsing하기 >>
                    // 미리 변수 타입을 알 수 있을 때 사용
                    // 특정 라이브러리를 만들어서 key를 돌리거나 이것을 가지고 반복하는 등 직접 노드를 건드려야 할 때 사용

                    // 전체 노드로 가져오기
                    JsonNode jsonNode = objectMapper.readTree(json);
                    
                    // 일반적인 Object에 접근하여 parsing하는 방법
                    String _name = jsonNode.get("name").asText();
                    int _age = jsonNode.get("age").asInt();
                    System.out.println("name : "+_name);
                    System.out.println("age : "+_age);

                    // **Array 노드에 접근하여 parsing 방법**

                    // car List의 값을 그냥 String으로 가져오면 제대로 출력되지 않음 (X)
                    //String _list = jsonNode.get("cars").asText();
                    //System.out.println(_list);

                    // cars는 그 자체로 '하나의 새로운 노드'로 볼 수 있음!
                    // 1. 배열의 노드 (cars) 가져오기
                    JsonNode cars = jsonNode.get("cars");

                    // ArrayNode도 일종의 Object Mapper의 클래스
                    // 2. parsing한 뒤 형변환 시켜줌
                    ArrayNode arrayNode = (ArrayNode)cars;

                    // 3. ArrayNode에 대해서 다시 원하는 클래스로 매칭시킴
                    // objectMapper.convertValue() : Map을 객체로 바꾸거나 여러가지 object를 가지고 JSON이 아닌 우리가 원하는 클래스로 맵핑시킬 수 있음
                    // 매개변수로 TypeReference를 받음 : 우리가 받고자 하는 generic Type을 TypeReference안에 넣어줌
                    // object(arrayNode)를 받아서 우리가 원하는 타입(List<Car>)으로 변환시킴
                    List<Car> _cars = objectMapper.convertValue(arrayNode, new TypeReference<List<Car>>(){});
                    System.out.println(_cars);
                }
            }
            ```
        - 출력 결과
            ```shell
            > Task :Main.main()
            main
            {"name":"홍길동","age":10,"cars":[{"name":"K5","car_number":"11가 1111","TYPE":"sedan"},{"name":"Q5","car_number":"22가 2222","TYPE":"SUV"}]}
            name : 홍길동
            age : 10
            [Car{name='K5', carNumber='11가 1111', type='sedan'}, Car{name='Q5', carNumber='22가 2222', type='SUV'}]
            ```
        - 정리
            - 위와 같은 방식으로 JSON 노드에 접근하려면 해당 JSON이 어떻게 생겼는지 미리 표준 스펙을 알아야 함
            - 전체적인 JSON 노드 가져오기
                - JsonNode 클래스 사용
                - objectMapper.readTree() 메서드 사용
                - `JsonNode jsonNode = objectMapper.readTree(json);`
            - 일반적인 Object에 접근하여 parsing
                1. jsonNode.get("Object이름") : Object 가져옴
                2. .asText()나 .asInt()로 형변환
            - Array 노드에 접근하여 parsing
                1. jsonNode.get("Object이름") : Object 가져옴
                2. ArrayNode로 형변환 (ArrayNode)
                3. parsing을 하기 위해 `objectMapper.convertValue()` 사용
                    - Object와 원하는 타입(TypeReference)을 넣어서 맵핑!

    5. JSON 노드 안의 값 변경하기 🌟
        - jsonNode.set()함수는 막혀있음(사용 불가)
        - 대신 `ObjectNode` 클래스 사용
        - Main.java
            ```java
            public class Main {

                public static void main(String args[]) throws JsonProcessingException {
                    System.out.println("main");
                
                    ObjectMapper objectMapper = new ObjectMapper();
                    
                    User user = new User();
                    user.setName("홍길동");
                    user.setAge(10);

                    Car car1 = new Car();
                    car1.setName("K5");
                    car1.setCarNumber("11가 1111");
                    car1.setType("sedan");

                    Car car2 = new Car();
                    car2.setName("Q5");
                    car2.setCarNumber("22가 2222");
                    car2.setType("SUV");

                    List<Car> carList = Arrays.asList(car1, car2);
                    user.setCars(carList);

                    String json = objectMapper.writeValueAsString(user);
                    System.out.println(json);

                    // JSON 노드에 접근해서 parsing
                    JsonNode jsonNode = objectMapper.readTree(json);

                    String _name = jsonNode.get("name").asText();
                    int _age = jsonNode.get("age").asInt();
                    System.out.println("name : "+_name);
                    System.out.println("age : "+_age);

                    JsonNode cars = jsonNode.get("cars");
                    ArrayNode arrayNode = (ArrayNode)cars;
                    List<Car> _cars = objectMapper.convertValue(arrayNode, new TypeReference<List<Car>>(){});

                    System.out.println(_cars);

                    // 전체 노드(jsonNode)를 ObjectNode로 형변환 -> 값을 변경하기 위해
                    ObjectNode objectNode = (ObjectNode) jsonNode;

                    // 이름과 나이 변경 - put()이나 set()은 동일한 메서드
                    objectNode.put("name", "steve");
                    objectNode.put("age", 20);
                    
                    // toPrettyString() : JSON을 예쁘게 출력
                    System.out.println(objectNode.toPrettyString());
                }
            }
            ```

        - 출력 결과
            - JSON 노드 변경 완료
                ```shell
                > Task :Main.main()
                main
                {"name":"홍길동","age":10,"cars":[{"name":"K5","car_number":"11가 1111","TYPE":"sedan"},{"name":"Q5","car_number":"22가 2222","TYPE":"SUV"}]}
                name : 홍길동
                age : 10
                [Car{name='K5', carNumber='11가 1111', type='sedan'}, Car{name='Q5', carNumber='22가 2222', type='SUV'}]
                {
                "name" : "steve",
                "age" : 20,
                "cars" : [ {
                    "name" : "K5",
                    "car_number" : "11가 1111",
                    "TYPE" : "sedan"
                }, {
                    "name" : "Q5",
                    "car_number" : "22가 2222",
                    "TYPE" : "SUV"
                } ]
                }
                ```
            - JSON 노드 변경 전(sample.json)
                ```shell
                {
                "name":"홍길동",
                "age":10,
                "cars":[
                    {
                    "name":"K5",
                    "car_number":"11가 1111",
                    "TYPE":"sedan"
                    },
                    {
                    "name":"Q5",
                    "car_number":"22가 2222",
                    "TYPE":"SUV"
                    }
                ]
                }
                ```
        
- 총정리
    - Object Mapper를 통해서 각각의 JSON 노드에도 접근할 수 있다
    - AOP 또는 filter, intercepter에서 순수 JSON string으로 되어 있는 Body를 꺼내서 특정한 값을 변경할 때
        - 전체를 Object Mapper로 parsing해서 사용할 수도 있지만
        - 각각의 노드에 대해서도 설정을 바꾸고 값을 치환할 수 있음!
    