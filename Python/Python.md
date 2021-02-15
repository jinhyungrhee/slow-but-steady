# Point 클래스 선언

- Point 클래스는 2차원 평면의 점(또는 2차원 벡터)을 나타내는 클래스
    - 필요한 멤버는 점의 x-좌표와 y-좌표
- 선언
    - 생성함수(magic method 중 하나) __init__의 매개변수로 두 좌표 값을 받음. default 좌표 값은 0으로 정함. (다른 default 값으로 지정해도 됨)
    - [주의] 클래스의 모든 메서드의 첫 번째 매개변수는 **self**여야 함!(*self는 이 메서드를 호출하는 객체를 나타냄*)
    - *magic method(special method)란 파이썬이 내부적으로 구현한(빌트인) 메서드, 더블 언더스코어로 앞뒤를 감싼 형태*
    ```py
    class Point:
        def __init__(self, x=0, y=0):
            self.x = x  # x-좌표를 위한 멤버 self.x
            self.y = y  # y-좌표를 위한 멤버 self.y

    p = Point(1, 2)
    print(p)
    ```
    - 결과 : <__main__.Point object at 0x7fa115093438>와 같은 메시지 출력
        - print(p)를 수행하면 객체 p를 프린트해야 하는데, 구체적으로 어떤 내용을 출력해야 하는지 print 함수는 알지 못함.
        - *print 함수에게 어떤 내용을 출력해야 하는지 알려주는 magic method가 __str__함수임*.
        - print(p)를 실행할 때 p가 속한 클래스 Point에 __str__함수가 정의되어 있다면 호출함. 이 **__str__함수는 출력용 문자열을 리턴**하는데, **print 함수는 단순히 리턴된 문자열을 출력하는 역할**임.
        - 만약 __str__함수가 정의되어 있지 않다면, 해당 객체의 기본 정보인 '<__main__.Point object at 0x7fa115093438>'를 출력함

    - __str__함수 추가. __str__함수는 Point 객체의 출력하고 싶은 내용을 문자열로 만들어 리턴함.
        - (1, 2)와 같이 좌표 값을 일반적인 형식으로 출력하려 함
        - ```f"({self.x}, {self.y})"```py 형식의 f-문자열은 {} 안에 오는 변수를 변수의 값으로 교체해 문자열을 만드는 방법임.
        ```py
        class Point:
            def __init__(self, x=0, y=0):
                self.x = x
                self.y = y

            def __str__(self):
                return f"({self.x}, {self.y})"

        p = Point(1, 2) # x = 1, y = 2인 객체 생성
        print(p)        # p.__str__()이 호출되고 리턴된 "(1, 2)"를 출력함
        ```
    - int 클래스에서 magic method인 __str__을 자동으로 호출하는 방식
        ```py
        a = 10
        print(str(a))
        ```
        - int 클래스의 __str__함수는 해당 값을 문자열로 리턴하기 때문에 결국 문자열"10"이 출력됨.

    - Point 클래스에 적용
        ```py
        class Point:
            def __init__(self, x=0, y=0):
                self.x = x
                self.y = y

            def __str__(self):
                return f"({self.x}, {self.y})"

        p = Point(1, 2)
        s = str(p)  # p.__str__() 형식으로 호출됨
        print(s)    # s = "(1, 2)"

        ```
