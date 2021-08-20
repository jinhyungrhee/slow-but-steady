# POST Method

- POST
    - 리소스 생성, 추가
    - CREATE
    - 요청할 때마다 매번 데이터 생성하기 때문에 멱등성, 안정성 X
    - Path Variable 사용
    - Query Parameter를 설정할 수 있지만 일반적으로는 사용 X
        - 생성된 data를 전달받기 때문에 따로 조회할 필요 X (조회는 GET Method)
    - Data Body에 data를 실어서 보냄
        - 굳이 Query Parameter로 다른 데이터를 보낼 필요 없음

- 웹에서 데이터를 주고받는 형식
    1. XML
    2. JSON -> 거의 대부분의 API는 JSON 사용

- JSON
    - String : value
    - number : value
    - boolean : value
    - object : value { }
    - array : value [ ]
    ```js
    {
        "phone_number" : "010-1111-2222",
        "age" : 10,
        "isAgree" : false,
        "account" : {
            "address" : "steve@gmail.com",
            "password" : "1234",
        }
    }

    // user_list 조회하는 경우
    // 동일한 key-value값(account-password)에 대해서 배열의 형태로 리턴하는 JSON
    // 같은 key-value값을 가진 obejct들이 쭉 나열되어 있는 것
    {
        "user_list" : [
            {
                "account" : "abcd",
                "password" : "1234"
            },
            {
                "account" : "aaaa",
                "password" : "1111"
            },
            {
                "account" : "bbbb",
                "password" : "2222"
            }
        ]
    }

    {
        "account" : "abcd",
        "password" : "1234",

    }
    ```

- 예제 : 요청에 대한 JSON

    ```js
    {
        "account" : "",
        "email" : "",
        "password" : "",
        "address" : ""
    }
    ```

- POST를 선택하면 content type이 default로 `JSON`임
    - JSON은 기본적으로 encoding이 `UTF-8`임!

- spring-boot에서 POST 요청 받기
    1. Map 사용
    ```java
    @RestController
    @RequestMapping("/api")
    public class PostApiController {

        
        // POST 요청을 보낼 때 body에 데이터를 실었기 때문에 @RequestBody 붙여야 함!
        // 1.Map 사용
        // 어떤 값을 보낼지 미리 알아야 하지만 Map으로는 알기 어려움 => dto 작성!
        @PostMapping("/post")
        public void post(@RequestBody Map<String, Object> requestData){
            requestData.forEach((key, value) -> {
               System.out.println("key : " + key);
                System.out.println("value : " + value);
            });
        }
    }
    ```
    2. DTO 사용
    ```java
    @RestController
    @RequestMapping("/api")
    public class PostApiController {

        @PostMapping("/post")
        public void post(@RequestBody PostRequestDto requestData){
            // toString 메서드 사용해서 출력
            System.out.println(requestData);
        }
    }
    ```
    - PostRequestDto.java
    ```java
    import com.fasterxml.jackson.annotation.JsonProperty;

    // 아직 lombok은 모르기 때문에 get/set method 직접 만들어서 mapping!
    public class PostRequestDto {
        // 필요한 변수들 먼저 정의
        // 요청하는 JSON의 key에 해당하는 값들임
        private String account;
        private String email;
        private String address;
        private String password;
        // java에서는 camelCase로 작성되어 있지만 보내는 쪽에서는 snake_case로 작성한 경우 => 결과값으로 null 리턴됨
        // (object mapper라는 라이브러리를 통해서 text data가 object로 바뀌게 되는데 
        //  따로 이름을 지정해주지 않으면 snake_case로 찾아가서 camel case는 찾지 못함!)
        // 이 상황에서 매칭해줄 수 있는 방법 - @JsonPropery("이름") 지정 : 특정 이름에 대해서 매칭 가능
        // camel도 snake도 아닌 대문자로만 이루어진 약어 같은 경우에 사용하기 위해 존재함
        @JsonProperty("phone_number")
        private String phoneNumber; // phone_number

        @JsonProperty("OTP") // camel도 snake도 아닌 단어에 매칭
        private String OTP;
        // OTP는 getter/setter 설정 안해줬는데도 정상 작동... 왜지?

        public String getPhoneNumber() {
            return phoneNumber;
        }

        public void setPhoneNumber(String phoneNumber) {
            this.phoneNumber = phoneNumber;
        }

        // 상단바 Code-Generate-Getter&Setter-shift키 눌러서 전체선택 후 OK
        public String getAccount() {
            return account;
        }

        public void setAccount(String account) {
            this.account = account;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getAddress() {
            return address;
        }

        public void setAddress(String address) {
            this.address = address;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }

        // toString 오버라이딩
        @Override
        public String toString() {
            return "PostRequestDto{" +
                    "account='" + account + '\'' +
                    ", email='" + email + '\'' +
                    ", address='" + address + '\'' +
                    ", password='" + password + '\'' +
                    ", phoneNumber='" + phoneNumber + '\'' +
                    ", OTP='" + OTP + '\'' +
                    '}';
        }
    }

    ```

- PostRequestDto 결과

`PostRequestDto{account='user01', email='steve@gmail.com', address='패스트캠퍼스', password='abcd', phoneNumber='010-1111-2222', OTP='12345'}`

- Q. OTP getter&setter 설정하지 않아도 작동하는 이유? (POST 강의)