# 코드 커버리지(테스트 커버리지)

## Jacoco

- Java 코드의 코드 커버리지를 체크하는 라이브러리
    - 내가 작성한 테스트 코드가 어디까지 커버 가능한가?
- 결과를 html, xml, csv로 확인 가능함
- build.gradle plugins에 추가
    ```java
    plugins {
        id 'org.springframework.boot' version '2.5.4'
        id 'io.spring.dependency-management' version '1.0.11.RELEASE'
        id 'java'
        id 'jacoco'
    }
    ```
- jacoco 리포트가 나오기 위해서는 반드시 test가 우선 실행되어야 함
    1. 우측 gradle 탭 - Tasks - Verification - `test` 더블 클릭 (터미널에서 gradle 명령어로도 가능)
        - 실행 후 터미널에서 실행 결과를 확인할 수 있음(문제 유/무)
        - build 디렉토리에 reports라는 디렉토리가 생성되고 그 안에 있는 index.html을 실행시키면 test결과 구체적으로 확인 가능!
    2. 우측 gradle 탭 - Tasks - Verification - `jacocoTestReport` 더블 클릭
        - build/reports/jacoco/index.html 확인
        - 어느 코드가 테스트되었고 테스트되지 않았는지 확인 가능
            - controller는 100% 테스트되었음
            - dto는 거의 테스트되지 않음