# Spring Boot

- Spring Boot란?

    - Spring Boot는 간단하게 실행되며, **프로덕션 제품 수준의 스프링 기반 어플리케이션을 쉽게 만들 수 있음!**

    - Spring Boot 어플리케이션에는 **Spring 구성이 거의 필요하지 않음**

    - Spring Boot **java -jar로 실행하는 Java 어플리케이션**을 만들 수 있음!

    - Spring Boot 자체에서 tomcat도 내장함

- 주요 목표

    - Spring 개발에 대해 빠르고, 광범위하게 적용할 수 있는 환경

    - 기본값 설정만으로도 어플리케이션 실행 가능(기본값 설정 변경 가능)

    - 대규모 프로젝트에 공통적인 비 기능 제공 (보안, 모니터링 등등)

    - XML 구성 요구사항이 전혀 없음
        - annotation 기반으로 변경됨

- Build Tool (2가지)

    1. Maven (version : 3.3+)
    2. **Gradle** (version : 4.x (4.4+) and 5.x)  

- Servlet Containers (선택 가능)

    1. **Tomcat 9.x** (servlet version : 3.3)
    2. Jetty 9.4 (servlet version : 3.1)
    3. Undertow 2.0 (servlet version : 4.0)
    4. Netty

- 정리

    - 어플리케이션 개발에 필수 요소들만 모아두었음

    - 간단한 설정으로 개발 및 커스텀이 가능함
        - 기존 XML기반에서 annotation 기반 설정으로 변경됨(간단)
    
    - 간단하고 빠르게 어플리케이션 실행 및 배포가 가능함
        - jar 파일로 패키징
        - java가 설치되어 있는 어떤 곳이든지 웹 서버 어플리케이션 실행이 가능함
    
    - 대규모 프로젝트(운영환경)에 필요한 비 기능적 기능도 제공함

    - 오랜 경험에서 나오는 안정적인 운영이 가능함

    - Spring에서 불편한 설정이 없어졌음 (XML 설정 등)
        - 기존 '자바는 느리다', '프로토타이핑 하기에는 어렵다'와 같은 부분들이 보완됨