# 객체지향

1. 객체지향의 등장
- 1970년대 등장
- 이전 절차지향 언어의 문제점
    - 절차지향 언어 : 실행하고자 하는 순서대로 명령어를 입력해서 실행 (c언어)
    - 간단한 Logic을 순차적으로 처리하여 결과를 얻는 방식
    - 하지만 컴퓨터의 발전과 프로그램이 복잡해지면서 절차지향 언어의 비효율 발생(유지보수, 개발기간↑)
    - 이를 해결하기 위해 **효과적인 개발방식**을 채택하게 됨!
        - 추상화
        - 상속
        - 은닉
        - 재사용
        - 인터페이스 등
    - 객체지향 : 실제로 존재하는 사물을 있는 그대로 모델링하여 이들의 행위와 속성을 정의, 객체가 중심이 되어 실제 사물이 동작하는 방식으로 설계
        - 사물에 대해서는 `객체(obejct)`라고 부르며, 사물의 하는 `행위(method)`를 정의하고 해당 사물이 가지는 속성을 `변수(variable)`라고 정의
        - 절차지향 보다 더 편리한 설계 가능
    - Java : 어떠한 운영체제에서도 자바 가상머신(JVM)만 있으면 독립적으로 실행될 수 있도록 설계
        - 여러 플랫폼에서의 호환성을 제공함

2. 객체 설계하기
- 객체 == 사물 == Object
- ex : 자동차
    - 속성
        - 자동차 이름
        - 자동차 번호
        - 등록년월
        - 모델명
    - 행위
        - 주행거리 계산
        - 연비계산
        - 번호교체
        - 등록증 갱신

- 객체의 3가지 요소
    1. 상태 유지(객체의 상태)
        - 속성은 변수로 정의되어야 함.
        - 이러한 속성값이 바뀜으로써 객체의 상태가 변경될 수 있어야 함/
    2. 기능 제공(객체의 책임)
        - 캡슐화 연관
        - 객체가 제공하는 Method로 기능이 제공
    3. 고유 식별자 제공(객체의 유일성)
        - 특정 속성을 통해서 각각 고유한 값을 줄 수 있음
        - 이후 DB에서 Unique Key 또는 Primary Key로도 작성 가능

3. 물리 객체와 개념 객체
- 물리 객체
    - 실제로 사물이 존재하며 이를 클래스로 정의한 객체를 의미함
    - ex) 자동차 렌탈 시스템 : 자동차, 고객, 직원, 사업장, 정비소 등

- 개념 객체
    - 우리가 가밸할 웹 시스템에서 **Service**에 해당되며 이는 **Business logic을 처리하는 부분**을 의미
    - Business logic에서는 여러 객체를 서로 상호작용 하도록 하며 객체가 제공하는 오퍼레이션(Method)를 통해 객체의 속성을 변경시킴
    - ex) 사용자 관리 시스템 : 사용자 객체의 마지막 접속일자를 이용하여 계정만료, 비밀번호 초기화, 재등록 처리 등
        - 특정 Logic에 따라 사용자의 상태를 변경시키는 것
        - 이러한 판단은 객체가 하는 것이 아니라 중간의 Business logic이 하도록 설계 (주로 if문 사용)
        - 시스템마다 설정이 다를 수 있음!

- 객체지향에서의 코딩
    - 각 객체에 기능을 정의하고, 이를 business logic을 처리하는 Service에서 객체의 Method를 활용하여 여러 가지 조건을 확인하여 객체의 속성을 변경하는 작업
    - 이러한 작업을 위해 각 **객체의 속성**과 속성을 변경하고 상태를 변경할 수 있는 **오퍼레이션(Method)**을 잘 정의해야 함!