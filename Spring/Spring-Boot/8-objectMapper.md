# Object Mapper

- request나 response에 대해서는 `@RestController`가 자동적으로 object mapper의 역할을 수행
    - spring에서 내부적으로 request가 들어왔을 때 object로 바꿔줌
    - 반대로 object에서 string으로 바뀌어 response가 내려질 때도 동일한 역할 수행

- 만약 Controller외에 따로 작업이 필요한 경우 (객체를 JSON으로 바꿔야 하는 경우) 직접 `object mapper`를 생성한 뒤 `.writeValueAsString()`이나 `.readValue()`를 사용하여 object를 text(json)으로 바꾸거나 text(json)을 object로 바꿀 수 있음!

- Object Mapper

    - Text JSON을 Object로 변경하거나 반대로 Object를 Text JSON으로 변경하는 역할
    
    - object mapper 객체 생성
        ```java
        var objectMapper = new ObjectMapper();
        ```

    - 특징1) Object가 Text JSON으로 변환될 때에는 `get 메서드`를 활용함!
        - Class안에 getter() 생성 필요
        - `.writeValueAsString()` 사용
        ```java
        var user = new User("steve", 10, "010-1111-2222");
        var text = objectMapper.writeValueAsString(user);
        System.out.println(text);
        ```

    - 특징2) Text JSON이 object로 변환될 때에는 `default 생성자`가 필요함!
        - Class 안에 default 생성자 추가 필요
        - `.readValue()` 사용
        ```java
        var objectUser = objectMapper.readValue(text, User.class);
        System.out.println(objectUser);
        ```

    - User.java
        ```java
        public class User {
            private String name;
            private int age;

            @JsonProperty("phone_number") // snake_case로 동작하도록
            private String phoneNumber;
            
            // 에러 해결 2) default 생성자 추가
            public User() {
                this.name = null;
                this.age = 0;
                this.phoneNumber = null;
            }

            // 생성자 오버로딩
            public User(String name, int age, String phoneNumber){
                this.name = name;
                this.age = age;
                this.phoneNumber = phoneNumber;
            }

            // 에러 해결 1) get 메서드 추가


            public String getPhoneNumber() {
                return phoneNumber;
            }

            public String getName() {
                return name;
            }

            public int getAge() {
                return age;
            }

            // 자주하는 실수 - 사용자 지정 메서드 이름에 get을 포함했을 때 에러 발생!
            // object mapper가 해당 클래스에 대해서 serialize-deserialize할 때 에러 발생 가능
            // 내가 작성한 클래스가 object mapper에서 활용이 될 때는 get이 메서드 명에서 빠져야 함!
            // gtDefaultUser() -> defaultUser()
            public User defaultUser(){
                return new User("default", 0, "010-1111-2222");
            }

            // toString 메서드 오버라이딩

            @Override
            public String toString() {
                return "User{" +
                        "name='" + name + '\'' +
                        ", age=" + age +
                        ", phoneNumber='" + phoneNumber + '\'' +
                        '}';
            }
        }
        ```