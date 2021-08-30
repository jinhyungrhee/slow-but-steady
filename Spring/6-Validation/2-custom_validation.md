# Custom Validation

## Valid Annotation

- 방법
    - 내가 원하는 어노테이션을 특정한 변수 위에 지정
    - 내가 검사하고자 하는 클래스(객체)에 @Valid 어노테이션 지정

- 한 번 클래스에 지정해놓았기 때문에 재사용하기 매우 편리
- 하지만 작성하다 보면 **예외 케이스**가 반드시 등장!
    - 예를들어, 날짜 관련 Request 보낼 때 ISO표준규격 대신 String(YYYY-MM-DD)형태로 보냄. 이 경우 @Past나 @Future은 사용할 수 없음.
    - `@AssertTrue/False`를 사용하면 해결 가능

## Custom Validation

1. AssertTure/False와 같은 **method 지정**을 통해서 Custom Logic 적용 가능 (Method로 구현)

    - reqYearMonth 변수에 @Size annotation 적용
        - dto/User.java
            ```java
            // .. 생략 ..

            @Size(min = 6, max = 6)
            private String reqYearMonth; //yyyyMM
            ```
        - 이 경우 6자리 제한은 유효하지만 "a11111"과 같은 이상한 값도 유효성 검사를 통과할 수 있음
    - @AssertTrue 어노테이션 사용
        - **boolean type 리턴 메서드**와 매칭!
            - boolean type을 리턴하는 메서드 이름은 반드시 is로 시작해야 함! 
        - @AssertTrue 어노테이션 추가
            - return이 True면 정상 False면 비정상
        - dto/User.java
            ```java
            // .. 생략 ..

            @AssertTrue(message = "yyyyMM의 형식에 맞지 않습니다.")
            public boolean isReqYearMonthValidation(){
                // YearMonth parsing하기
                // 기본적으로 LocalDate이므로 yyyyMM"dd"까지 들어감
                // 날짜가 맞지 않으면 예외가 발생함
                try{
                    LocalDate localDate = LocalDate.parse(getReqYearMonth() + "01", DateTimeFormatter.ofPattern("yyyyMMdd"));
                }catch (Exception e){
                    // parsing이 제대로 안되었거나 날짜가 맞지 않으면 false 리턴
                    return false;
                }
                // parsing이 성공적으로 된 경우 true 리턴
                return true;
            }
            ```
        - ❗하지만 이 경우 재활용이 불가능함❗
            - dto/User.java에 작성을 해놓았는데 만약 dto/Req.java 클래스에서도 "yyyyMM"의 형태로 요청을 받는다고 했을 때 다시 새로 코드를 작성해주어야 함!
            - 동일한 코드의 중복이 엄청나게 발생함!
            - 이러한 **코드의 중복을 해결**하는 방법  
                ➡ **annotation 직접 만들기**  
                ➡ annotation 내부 `@Contraint(ValidatedBy = { })` 부분이 핵심!


2. ConstraintValidator를 적용(상속)하여 **재사용이 가능**한 Custom Logic 적용 가능 (Custom Annotation 구현)

    - Custom annotation 직접 만들기
        - annotation 패키지 - YearMonth 어노테이션 생성
        - 기존 annotation(@Email, @Patttern)에서 필요한 부분(default 부분) 가져오기
            ```java
            // @Constraint : 어떤 클래스를 가지고 검사할 것인지(YearMonthValidator를 통해 검사가 진행됨)
            @Constraint(validatedBy = {YearMonthValidator.class})
            @Target({ METHOD, FIELD, ANNOTATION_TYPE, CONSTRUCTOR, PARAMETER, TYPE_USE })
            @Retention(RUNTIME)
            public @interface YearMonth {
                String message() default "{javax.validation.constraints.Email.message}";

                Class<?>[] groups() default { };

                Class<? extends Payload>[] payload() default { };

                // @Pattern에서 가져옴 - default값 지정(사용자가 직접 패턴을 넣지 않아도 기본 패턴인 "yyyyMM"으로 적용됨)
                String pattern() default "yyyyMM";
            }
            ```
    - 우리가 만든 annotation을 활용할 클래스 만들기
        - **실제 검사를 진행하는 클래스** 생성
            - 위 어노테이션과 이 클래스가 User객체의 @AssertTrue 어노테이션을 대체함
            - 재사용성 확보
        - validator 패키지 - YearMonthValidator 클래스 생성
            - **ConstraintValidator** 상속받아 사용
        - validator/YearMonthValidator.java
            ```java
            // ConstraintValidator 상속 받음
            // 두 가지 타입 받음 : 1)우리가 원하는 어노테이션(YearMonth) 2) 거기에 들어갈 값 지정
            public class YearMonthValidator implements ConstraintValidator<YearMonth, String> {
                
                private String pattern;

                @Override
                public void initialize(YearMonth constraintAnnotation) {
                    //ConstraintValidator.super.initialize(constraintAnnotation); // default로 생성됨(?)
                    
                    // ** 1.초기화(initialize)했을 때는 annotation에 지정된 패턴을 가져옴 **
                    this.pattern = constraintAnnotation.pattern();
                   
                }

                @Override
                public boolean isValid(String value, ConstraintValidatorContext context) {
                    // 검사할 값이 들어옴 (value == 'yyyyMM')
                    // assertTrue에서 사용했던 try-catch문 가져옴 -> 더이상 User의 @assertTrue는 필요 없음
                    try{
                        // "01"을 붙여줘야 자동적으로 month에 대해서 검색이 됨
                        // "dd"를 붙이는 이유 : LocalDate이기 때문에 날짜가 있어야 함 - "dd"가 없으면 에러가 발생하기 때문에 모든 월에 존재하는 날짜(=01)를 붙여준 것
                         // ** 2.annotation에 지정한 패턴의 형태(this.pattern)로 value값이 잘 들어가 있는지 확인 **
                        LocalDate localDate = LocalDate.parse(value+"01", DateTimeFormatter.ofPattern(this.pattern));
                    }catch (Exception e){
                        // parsing이 제대로 안되었거나 날짜가 맞지 않으면 false 리턴
                        return false;
                    }

                    // parsing이 성공적으로 된 경우 true 리턴
                    return true;
                }
            }
            ```

        - 에러 발생
            - `DateTimeParseException: Text '20210401' could not be parsed at index 0`
                - parsing이 제대로 이루어지지 않아서 발생
            - LocalDate.parse(value+"01", DateTimeFormatter.ofPattern(this.pattern));
                - value : "202104"
                - pattern : "yyyyMM"
                    - 우리는 "01"까지 붙였기 때문에 "yyyyMMdd"까지 되어야 함
            - 해결방법
                - YearMonth 어노테이션(YearMonth.java)의 default String pattern에 "dd"추가
                    ```java
                    // ... 생략 ...

                    String pattern() default "yyyyMMdd";
                    ````
                - 이유
                    - YearMonthValidator에서 1.초기화 시 default 패턴인 "yyyyMM"을 가져왔음
                    - 우리가 parsing할 때 "01"을 붙여주었기 때문에 실제 값은 "20210401"이 됨
                      - 하지만 실제 외부로 보여지는 것, 입력된 것은 "202104"임
                    - 따라서 올바르게 패턴이 매칭되려면 default 패턴값을 "yyyyMMdd"로 변경해야 함  
                    ➡ **사용자는 실제로 "yyyyMM"까지만 입력했지만 실제로 내부 로직에서 처리될 때는 자연적으로 dd까지 붙여서 "yyyyMMdd"로 처리되는 것**

    - 정리
        - 이렇게 생성된 Custom Annotation은 다른 어떤 dto 클래스가 만들어지더라도 간단히 붙여서 사용할 수 있음
            - ❗코드의 중복 해결, 재사용성이 확보됨❗

3. 더 알아보기 (보너스 예제)
    - object_mapper 예제에서 사용했던 Car dto 사용(복사/붙여넣기)
    - dto/User.java
        - User 클래스 안에 Car list 가지고 있는 형태
        ```java
        public class User {

            @NotBlank
            private String name;
            @Max(value = 90)
            private int age;

            // User 하위에 Car list 추가
            // Car에 대한 Validation은 Car 클래스 안에서 생성
            private List<Car> cars;

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
        - Car 모든 변수에 @NotBlank(공백 허용X) 어노테이션 붙임
        ```java
        public class Car {
            @NotBlank
            private String name;

            @NotBlank
            @JsonProperty("car_number")
            private String carNumber;

            @NotBlank
            @JsonProperty("TYPE")
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

    - 하지만 공백이 담긴 Request보내도 에러 발생 X
        - JSON Request Body
            ```js
            {
            "name":"홍길동",
            "age":10,
            "cars":[
                {
                "name":"K5",
                "car_number":"",
                "TYPE":""
                },
                {
                "name":"Q5",
                "car_number":"",
                "TYPE":""
                }
            ]
            }
            ```
        - JSON Response Body
            - status code : 200
            ```js
            {
            "name": "홍길동",
            "age": 10,
            "cars":[
            {
            "name": "K5",
            "car_number": "",
            "TYPE": ""
            },
            {
            "name": "Q5",
            "car_number": "",
            "TYPE": ""
            }
            ]
            }
            ```

    - 원인 : **특정 클래스나 변수에 대해서 검사하고 싶으면 @Valid 어노테이션 꼭 붙여야 함!**
        - 이미 검사하고 있는 클래스 안에 포함되어 있으니까 자동적으로 될 것이라 생각할 수 있음 -> ❌
        - ❗독립적인 클래스인 경우 직접 **@Valid** 어노테이션을 꼭 붙여줘야 함❗
            ```java
            public class User {

                @NotBlank
                private String name;
                @Max(value = 90)
                private int age;

                // User 하위에 Car list 추가
                // Car에 대한 Validation은 Car 클래스 안에서 생성
                // 해당 클래스에 대해서 검사하고 싶으면 @Valid 붙이기
                @Valid
                private List<Car> cars;

            // .. 생략 .. 
            ```
        - 정리
            - 클래스 안에 다른 객체가 있고 그것이 Object 형태일 경우, @Valid를 반드시 붙여줘야 그 안에 존재하는 어노테이션들이 정상적으로 검사할 수 있음
