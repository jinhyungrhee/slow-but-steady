# AOP

- AOP(Aspect Oriented Programming)
    - 관점지향 프로그래밍
    - 스프링 어플리케이션은 대부분 특별한 경우를 제외하고 MVC 웹 어플리케이션에서 `Web Layer`, `Business Layer`, `Data Layer`로 정의
        - Web Layer : REST API를 제공하며 Client 중심의 로직 적용 (response, HTTP status)
        - Business Layer : 내부 정책에 따른 logic을 적용 및 개발하며, 주로 해당 부분을 개발
        - Data Layer : 데이터 베이스 및 외부와의 연동을 처리

- 횡단 관심
    - Method Parameter Log 
        - 메서드에 들어가는 parameter, argument들을 찍어서 이 메서드가 실행될 때 어떠한 값이 들어가고 끝났을 때 어떠한 값이 리턴되었는지 확인
    - 실행시간 Log 
        - 특정 메서드의 실행 시간 확인
    - Parameter Encode
        - 메서드가 들어갈 때 변환된 값, 리턴 시 변환된 값 확인
        - 사실 이러한 패턴은 좋지는 않지만 현업에서 꼭 필요할 수도 있음 
    - 정리
        - AOP는 Method나 특정 구역에 반복되는 logic들을 한 곳으로 모아서 코딩할 수 있게 해줌 (직접 해봐야 이해 쉬움)

- 주요 Annotation

    |Annotation|의미|
    |--|--|
    |@Aspect|자바에서 널리 사용하는 AOP 프레임워크. AOP를 실행하고 싶은 Class에 할당|
    |@Pointcut|기능을 어디에 적용시킬지 설정. 메서드나 어노테이션 등 AOP를 적용시킬 지점을 설정|
    |@Before|어떠한 메서드가 실행되기 이전에 실행하려는 메서드에 할당|
    |@After|어떤 메서드가 성공적으로 실행된 다음에, 예외가 발생되더라도 실행시키려는 메서드에 할당|
    |@AfterReturning|메서드가 성공적으로 실행이 된 다음, 정상적으로 리턴이 되었을 때 실행되는 메서드에 할당(Not Throws)|
    |@AfterThrowing|메서드가 호출 된 후에 예외가 발생하면 실행되는 메서드에 붙임|
    |@Around|Before/after를 모두 제어할 수 있음. 예외가 발생하더라도 실행할 수 있는 메서드에 지정|