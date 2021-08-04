# 객체지향 설계 5원칙(SOLID)

- 응집도와 결합도
    - 좋은 소프트웨어 설계를 위해서는 결합도(coupling)는 낮추고 응집도(cohesion)는 높여야 함!
    - 결합도
        - 모듈(클래스)간의 **상호 의존도**를 나타내는 지표
        - 결합도가 낮으면 모둘간의 상호 의종성이 줄어들어 객체의 재사용 및 유지보수 편리
    
    - 응집도
        - 하나의 모듈 내부에 존재하는 구성 요소들의 **기능적 관련성**
        - 응집도가 높은 모듈은 하나의 책임에 집중하고 독립성이 높아져 재사용 및 유지보수가 용이

1. SRP(Single Resposnibility Principle) : 단일 책임 원칙
    - 어떠한 클래스를 변경해야 하는 이유는 단 한가지 뿐이여야 한다
    - 분리 전
    ```java
    class Unit {
        private String name;
        private int speed;

        public void attack() {

        }
        
        public void move() {
            if(name.equals("저글링")){
                speed += 3
            }else if(name.equals("탱크")){
                if("탱크모드"){
                    speed = 0
                }else{
                    speed = 10
                }
            }else if(name.equals("정찰기")){
                speed = 15
                충돌 = false
            }
        }
    }
    ```
    
    - 분리 후
    ```java
    class 저글링 extends Unit {
        public void move() {
            this.speed += 3
        }
    }
    class 탱크 extends Unit {
        public void move() {
            if("탱크모드") {
                speed = 0
            }else{
                speed = 10
            }
        }
    }
    class 정찰기 extends Unit {
        public void 정찰기() {
            this.충돌 = false
        }
        public void move() {
            speed = 15
        }
    }
    ```

2. OCP(Open Closed Principle) : 개방 폐쇄 원칙
    - 자신의 확장에는 열려 있고 주변의 변화에 대해서는 닫혀 있어야 한다
    - 상위 클래스 또는 인터페이스를 중간에 둠으로써, 자신은 변화에 대해서 폐쇄적이지만 인터페이스는 외부의 변화에 대해서 확장을 개방해줄 수 있다
    - 이 부분은 JDBC와 Mybatis, Hibernate 등 JAVA에서는 Stream(Input, Out)에서 찾아볼 수 있음

3. LSP(Liskov Substitution Principle) : 리스코프 치환 원칙
    - 서브 타입은 언제나 자신의 기반 타입(상위 타입)으로 교체할 수 있어야 한다

4. ISP(Interface Segregation Principle) : 인터페이스 분리 원칙
    - 클라이언트는 자신이 사용하지 않는 메서드에 의존 관계를 맺으면 안 된다
    - **프로젝트 요구 사항과 설계에 따라서 SRP(단일책임원칙)/ISP(인터페이스분리원칙)를 선택**

5. DIP(Dependency Inversion Principle) : 의존 역전 원칙
    - 자신보다 변하기 쉬운 것에 의존하지 말아야 한다.