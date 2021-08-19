# GET Method

- 리소스 취득
- READ
- 멱등성
- 안정성
- Path Variable로 받을 수 있음
    ```java
    @RestController
    @RequestMapping("/api/get")
    public class getApiController {

        // GET Mapping(주소 지정) 방법 두 가지
        //방법1 : path라는 속성을 통해 명확하게 경로가 무엇인지 지정해주는 방법 (명시적으로 지정)
        @GetMapping(path="/hello") //http:localhost:9090/api/get/hello
        public String hello(){
            return "get Hello";
        }

        //방법2 : 예전 방법 = RequestMapping
        // RequestMapping은 get/post/put/delete 모두 지원 (ctrl + space로 메서드 속성에 GET 설정)
        @RequestMapping(path = "/hi", method = RequestMethod.GET) // get http://localhost:9090/api/get/hi
        public String hi(){
            return "hi";
        }
        
        // 변화하는 구간에 대해서는 path variable을 통해 받음
        // spring boot에서 path variable을 받는 방법

        // 기본적으로 GET방식으로 주소 지정하는 것은 동일
        
        // 상단 클래스에서 "/api/get"까지 매핑되어 있으므로 /get까지는 고정된 주소임
        // 주소에 대문자 사용 X (가독성)
        // http://localhost:9090/api/get/path-variable/{name}
        // 주의 : get mapping에 적어 놓은 {}안의 이름과 parameter 이름이 동일해야 함!!
        @GetMapping("/path-variable/{name}")
        public String pathVariable(@PathVariable String name){

            System.out.println("PathVariable : "+name);

            return name;
        }

        // 개발중에 path-variable 주소의 이름과 parameter이름을 다르게 설정해야 할 때
        //@GetMapping("/path-variable/{id}")
        //public String pathVariable(@PathVariable(name="id") String pathName){

        //    System.out.println("PathVariable : "+pathName);

        //    return pathName;
        //}
    ```

- Query Parameter로 받을 수 있음
    - ex) https://www.google.com/search?q=%EC%9D%B8%ED%85%94%EB%A6%AC%EC%A0%9C%EC%9D%B4&rlz=1C1SQJL_koKR912KR912&oq=%EC%9D%B8%ED%85%94%EB%A6%AC%EC%A0%9C%EC%9D%B4&aqs=chrome..69i57.1409j0j15&sourceid=chrome&ie=UTF-8
    - 검색을 할 때 사용하는 여러 가지 매개변수 인자
    - `?` 뒤에 나타나며 `&`로 key와 value 쌍이 구분됨
        - search?q = %EC%9D%B8%ED%85%94%EB%A6%AC%EC%A0%9C%EC%9D%B4
        - &rlz = 1C1SQJL_koKR912KR912
        - &oq = %EC%9D%B8%ED%85%94%EB%A6%AC%EC%A0%9C%EC%9D%B4
        - &aqs = chrome..69i57.1409j0j15
        - &sourceid = chrome
        - &ie = UTF-8
    - 이것들을 spring boot에서 받는 방법
    ```java
    // Query Parameter 받는 방법 (3가지)
    // https://localhost:9090/api/get/query-param?user=steve&email=steve@gmail.com&age=30
    // 1. Map으로 받는 방법 (모든 것을 다 받을 수 있어서 key가 무엇인지 알 수 없음)
    @GetMapping(path="query-param")
    public String queryParam(@RequestParam Map<String, String> queryParam){

        // Map자체를 리턴하면 값이 없기 때문에 String buffer에 담아서 리턴
        StringBuilder sb = new StringBuilder();

        queryParam.entrySet().forEach( entry -> {
            System.out.println(entry.getKey());
            System.out.println(entry.getValue());
            System.out.println("\n");

            sb.append(entry.getKey()+" = "+entry.getValue()+"\n");
        });

        return sb.toString();
    }
    
    // 2. RequestParam annotation을 각 변수에 붙여서 각각의 키를 명시 (key를 직접 지정) => 변수 늘어날수록 복잡(=> 'DTO 맵핑'으로 해결)
    @GetMapping("query-param02")
    public String queryParam02(
            @RequestParam String name,
            @RequestParam String email,
            @RequestParam int age
    ) {

        System.out.println(name);
        System.out.println(email);
        System.out.println(age);


        return name+" "+email+" "+age;
    }

    // 3. 제일 많이 쓰는 방법 DTO Mapping
    // dto 패키지 생성 + UserReqeust 클래스 생성 (getter & setter 생성)
    // RequestParam annotation 사용하지 않고 userRequest객체로 받음
    // ?user=steve&email=steve@gmail.com&age=30 여기에서 key에 해당하는 이름들을 해당 객체에서 변수들과 이름 매칭을 시켜줌
    // 미리 query parameter에 대해서 정의해 두었으면 이런식으로 객체를 만들어서 받는 형태로 사용하는 것이 가장 편리
    // 이 방식은 요청한 값에 대한 검증도 편리
    // ?user=steve&email=steve@gmail.com&age=30&address=서울 : 알 수 없는 값이 들어온 경우 해당 값(address)은 파싱이 되지 않고 누락됨
    @GetMapping("query-param03")
    public String queryParam03(UserRequest userRequest) {

        System.out.println(userRequest.getName());
        System.out.println(userRequest.getEmail());
        System.out.println(userRequest.getAge());


        return userRequest.toString();
    }
    ```
    - dto 패키지/UserRequest.java
    ```java
    package com.example.hello.dto;

    public class UserRequest {

        private String name;
        private String email;
        private int age;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        // toString 메서드 오버라이딩 - 자동완성 선택
        @Override
        public String toString() {
            return "UserRequest{" +
                    "name='" + name + '\'' +
                    ", email='" + email + '\'' +
                    ", age=" + age +
                    '}';
        }
    }
    ```