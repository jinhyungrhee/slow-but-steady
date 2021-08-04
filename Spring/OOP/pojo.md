# POJO JAVA

- POJO(Plain Old Java Object)
    - 순수한 자바 오브젝트 의미 (외부의 종속성 없이 순수하게 자바로 이루어진 클래스)
    - 예전에는 EJB의 인기로 순수 자바 오브젝트를 이용하지 않고 EJB에서 제공하는 클래스에 많이 의존했음
    - 그러다보니 Module의 교체, 시스템 업그레이드 시 종속성으로 인해 여러 가지 불편함 발생!    

- POJO 특징
    1. 특정 규약에 종속되지 않는다
        - 특정 Library, Module에서 정의된 클래스를 상속받아 구현하지 않아도 됨!
        - POJO가 되기 위해서는 외부의 의존성을 두지 않고 순수한 JAVA로 구성이 가능해야 함
    2. 특정 환경에 종속되지 않는다
        - 특정 비즈니스 로직을 처리하는 부분에 외부 종속적인 HTTP request, session등이 사용되면 POJO를 위배한 것으로 간주됨!
        - spring에서 많이 사용되는 @Annotation 기반으로 설정하는 부분도 엄연히 POJO라고 볼 수 없음!

- POJO Framework
    1. Spring, Hibernate
    - 이러한 POJO를 지키기 위해서 사용하는 프레임워크
    - 하나의 서비스를 개발하기 위해서는 시스템의 복잡함, 비즈니스 로직의 복잡함 등 다양한 어려움을 맞이하게 됨
        - 개발자가 시스템의 복잡함까지 챙기면서 비즈니스 로직의 복잡함까지 같이 개발하기는 매우 어려움 ➡ 프레임워크의 도움을 받는 이유
    - Spring과 Hibernate는 객체지향적인 설계를 하며 POJO를 지향함!
    - 개발자가 **서비스 로직에 집중**하고 이를 POJO로 쉽게 개발할 수 있도록 지원하는 프레임워크
    - 앞으로는 복잡한 엔터프라이즈 로직은 Spring, Hibernate에게 맡기고, 이들을 사용함으로써 많은 장점을 얻을 수 있음
        - spring 프레임워크가 오랜 기간, 전 세계적으로 사랑받는 이유임!
        - 객체지향적 설계가 이미 이루어져 있기 때문에 개발자는 서비스 로직에 집중할 수 있고 그러한 패러다임을 벗어나지 않도록 개발자들간의 코드를 맞춰줌!

## 주의사항 (챕터를 마치며..)

- 돌아보기
    - 자신의 코드에 if/else, switch 코드가 난무하고 있지는 않은가?
    - 책임과 역할이 다른 코드가 하나의 클래스에 다 들어가 있지 않은가?
    - 절차지향적으로 한 개의 파일에 모든 코드를 넣고 있지 않은가?
    - 내가 만든 객체가 재사용이 가능한가?