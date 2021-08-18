## REST Client 설치

- Talend API Tester 설치
    - GET 방식 외에 POST, PUT, DELETE 같은 HTTP Method를 테스트할 수 있는 툴
    - 설치 방법
        - 크롬 웹스토어 > rest api client 검색 > Talend API Tester - Free Edition 추가
    - 웹 어플리케이션을 개발한 다음에 해당 응답이 잘 오는지, 요청을 잘 받아주는지 확인 가능

## Hello Spring Boot

- spring boot를 통한 문자 리턴

- spring boot에서는 요청을 받는 부분을 **controller**라고 함!
    1. hello 패키지 아래 controller 패키지 생성
    2. controller 패키지 아래 ApiController 클래스 생성
    3. controller로 동작하기 위해서는 annotation으로 지정 ⭐
        - `@RestController` 명시
        - 자동으로 spring에서 REST API르 처리하는 Controller로 인식
    4. 주소 할당 ⭐
        - `@RequestMapping("주소")` 사용 : URI를 지정해주는 annotation

    5. GET 메서드로 "hello spring boot!"라는 문자열 response로 내려주기
        - public String hello() 메서드 생성
        - 주소 지정 ⭐ (GET방식으로 API 열어주기)
            - `GetMapping("주소")` : GET방식 사용 시
            - `http://localhost:9090/api/hello`라는 주소가 mapping이 됨! 

    - resources > application.properties 폴더에 `server.port=9090`로 사용하는 port번호 변경 가능!

    - 코드로 확인

        ```java
        package com.example.hello.controller;

        import org.springframework.web.bind.annotation.GetMapping;
        import org.springframework.web.bind.annotation.RequestMapping;
        import org.springframework.web.bind.annotation.RestController;

        @RestController // 해당 class는 REST API 처리하는 controller
        @RequestMapping("/api") // RequestMapping은 URI를 지정해주는 annotation
        public class ApiController {

            @GetMapping("/hello") // http://localhost:9090/api/hello
            public String hello(){
                return "hello spring boot!";
            }

        }
    ```