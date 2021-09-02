# Filter & Interceptor

## Filter

- Web Application에서 관리되는 영역
- Spring Boot Framework에서 Client로부터 오는 요청/응답 즉, 최최/최종 단계의 위치에 존재하는 것
- 이를 통해 요청/응답의 정보를 변경 가능
- Spring에 의해서 데이터가 변환되기 전의 순수한 Client의 요청/응답 값 확인 가능

- **유일하게 ServletRequest, ServletResponse의 객체를 변환할 수 있는 곳**

- 주로 Spring Framework에서는 **request/response의 Logging** 용도로 활용하거나 **인증과 관련된 Logic**들을 해당 Filter에서 처리
    - `예시 1` back-office 또는 Admin이라는 곳에서, 이 곳에 대한 모든 요청 또는 어떤 사용자가 들어왔고 어떤 것을 요청했는지에 관한 기록을 찍을 때
        - AOP의 경우 이미 객체로 mapping이 되었기 때문에 순수한 내용은 아님
        - Filter는 가장 앞단에서 Client의 요청이 들어오자마자 해당 Request Body나 Response Body를 기록함
    - `예시 2` 보안의 용도로 사용
        - 사용자 요청이 들어왔을 때 뒷단의 Interceptor를 타기도 전에 아예 앞단에서 세션 여부 등을 확인하여 reject하거나 unauthorized error를 발생시킴

- Filter에서 이러한 선처리/후처리를 통해 Service Business Logic과 분리시켜줌
    - Filter에서 순수하게 Request Header, Request Body, Response에 대한 기록들을 남김!

- AOP, Filter, Interceptor를 모두 걸어두면 Filter → Intercepter → AOP 순으로 동작
    - life cycle은 filter부터 시작됨!

## Filter에서 Client가 보낸 순수한 Request Body를 어떻게 기록하는지 확인

### Lombok 사용하기

- Lombok 활용
    - JAVA에서 사용하는 라이브러리
    - getter&setter, 생성자, toString 오버라이딩 등을 직접 작성하지 않고 깔끔하게 해결
        - `@Getter, @Setter` -> 변수의 Get, Set메서드 만들어줌
        - `@Data` -> getter&setter, hashcode(), toString(), equals()까지 전부 다 생성하여 lombok에서 관리
        - `@NoArgsConstructor` -> 기본생성자 생성(User()만 생성)
        - `@AllArgsConstructor` -> 전체생성자(User(String, int))
            - 왼쪽 하단 `Structure 탭`에서 확인 가능
    - lombok을 사용하면 getter&setter 만들 필요 없이 변수만 선언하고 @Data, @NoArgsConstructor, @AllArgsConstructor annotation만 붙여주면 됨!
    - dto/User.java
        ```java
        // lombok 사용
        //@Getter
        //@Setter
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public class User {

            private String name;
            private int age;

        }
        ```

    - lombok을 사용하는 Controller에는 `@Slf4j` 붙임
        - @Slf4j : lombok 사용시 Controller에 붙이는 어노테이션
        - lombok을 사용하면 Sysout 대신 log 사용 
            - 중괄호({})를 사용하여 문자열 뒤에 등장하는 객체와 매칭시킴
        - controller/ApiController.java
        ```java
        @Slf4j
        @RestController
        @RequestMapping("/api/user")
        public class ApiController {

            @PostMapping("")
            public User user(@RequestBody User user){
                // lombok을 사용하면 Sysout 대신 log 사용 - {} 사용(문자열 뒤의 객체와 매칭)
                log.info("User : {} , {}", user, user);

                return user;
            }
        }

        ```

     - 프로젝트 시작 시 lombok 설정 깜빡한 경우
        - buld.gradle 파일 dependencies에 코드 두 줄 추가
            ```
            compileOnly 'org.projectlombok:lombok'
            annotationProcessor 'org.projectlombok:lombok'
            ```
        - 컴파일 시 annotaionProcesor가 같이 동작하게 됨
        - 컴파일할 때만 lombok 사용(compileOnly)
            - User 클래스에 lombok 어노테이션을 붙여놓으면 Java Complier가 compile할 때 같이 complie하면서 getter&setter가 만들어지는 형태
            - 컴파일 시 이미 클래스 파일 안에다가 생성자나 getter&setter가 다 만들어 놓기 때문에 프로그램이 직접 실행될 때는 필요가 없다.

### Filter 생성

- filter 패키지 - GlobalFilter 클래스 생성
- Filter 상속받아 사용(javax.servlet.Filter)
- doFilter() 메서드 오버라이딩
- @Component로 filter 등록하기
    - Spring에 의해서 Bean으로 관리되도록 함