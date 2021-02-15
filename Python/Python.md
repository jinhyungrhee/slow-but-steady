# Point 클래스 선언

- Point 클래스는 2차원 평면의 점(또는 2차원 벡터)을 나타내는 클래스
    - 필요한 멤버는 점의 x-좌표와 y-좌표

- 선언
    - 생성함수(magic method 중 하나) __init__의 매개변수로 두 좌표 값을 받음. default 좌표 값은 0으로 정함. (다른 default 값으로 지정해도 됨)
    - [주의] 클래스의 모든 메서드의 첫 번째 매개변수는 **self**여야 함!(**self는 이 메서드를 호출하는 객체를 나타냄**)
    - magic method(special method)란 파이썬이 내부적으로 구현한(빌트인) 메서드, 더블 언더스코어로 앞뒤를 감싼 형태
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
        - print 함수에게 어떤 내용을 출력해야 하는지 알려주는 magic method가 __str__함수임.
        - print(p)를 실행할 때 p가 속한 클래스 Point에 __str__함수가 정의되어 있다면 호출함. 이 **__str__함수는 출력용 문자열을 리턴**하는데, **print 함수는 단순히 리턴된 문자열을 출력하는 역할**임.
        - 만약 __str__함수가 정의되어 있지 않다면, 해당 객체의 기본 정보인 '<__main__.Point object at 0x7fa115093438>'를 출력함

    - __str__함수 추가. __str__함수는 Point 객체의 출력하고 싶은 내용을 문자열로 만들어 리턴함.
        - (1, 2)와 같이 좌표 값을 일반적인 형식으로 출력하려 함
        - ```f"({self.x}, {self.y})"``` 형식의 f-문자열은 **{}** 안에 오는 변수를 변수의 값으로 교체해 문자열을 만드는 방법임.
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

# Point 클래스 메쏘드 - 연산자 오버로딩

- 메쏘드는 __init__, __str__, __len__ 등과 같은 특별 메쏘드(magic method)와 일반 메쏘드로 나뉨.
    - 특별 메쏘드(magic method)의 이름은 두 개의 underscore로 감쌈.

- Magic method의 예
    - Point 객체는 점을 나타내지만 벡터(vector)로 생각할 수 있음.
    - 두 점을 더하는 연산을 하려면 다음과 같은 일반 메쏘드 작성 => 각 좌표 값을 더해서 새로운 점을 생성해 리턴
    ```py
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)

    p = Point(1, 2)
    q = Point(3, 4)
    r = p.add(q)
    print(r)    # r =(4, 6)
    ```

- ### 연산자 오버로딩(Overloading)
    - 정수, 실수 덧셈처럼 ``` r = p + q ```의 형식으로 **+** 연산자를 사용할 수 있다면 직관적이고 더 이해하기 쉬움. 파이썬에서는 이를 위한 특별 메쏘드(__add__)를 제공함.
    - 정수, 실수의 덧셈 **+** 연산자에 Point 클래스의 덧셈 연산을 **덧입혔다**는 의미에서 이를 **"연산자 overloading"**이라고 함.
    - 연산자 오버로딩의 예:
    ```py
    def __init__(Self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):   # 덧셈 연산자 오버로딩
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # 뺄셈 연산자 오버로딩
        return Point(self.x - other.x, self.y - other.y)

    p = Point(1, 2)
    q = Point(3, 4)
    r = p + q
    s = p - q
    print(r)    # r = (4, 6)
    print(s)    # s = (-2, -2)
    ```
    - ```r = p + q```를 하면, 실제로는 ```r = p.__add__(q)```가 호출되고 두 벡터의 합 벡터가 리턴되어 r에 저장됨.
    - ```s = p - q```를 하면, 실제로는 ```s = p.__sub__(q)```가 호출되고 두 벡터의 차 벡터가 리턴되어 s에 저장됨.

    - 산술 연산자 오버로딩:
        - __add__ : +
        - __sub__ : -
        - __mul__ : *
        - __truediv__ : /
        - __floordiv__ : //
        - __mod__ : %
        - __iadd__ : +=
        - __isub__ : -=
        - __imul__ : *=
        - __itruediv__ : /=
        - __ifloordiv__ : //=
        - __imod__ : %=
        
    - 비교 연산자 오버로딩:
        - __lt__ : <
        - __le__ : <=
        - __gt__ : >
        - __ge__ : >=
        - __eq__ : ==
        - __ne__ : !=

    - 벡터의 곱셈 연산
        - **scalar * vector 형식** : ```r = 3 * p```처럼 p의 좌표 값에 모두 상수 3을 곱하는 식으로 사용됨
        - scalar 값은 Point 객체가 아니기 때문에 **연산에 참여하는 두 객체의 타입이 같지 않다**는 문제 발생.
        - 이러한 경우에도 연산자 오버로딩 기능 지원. 단 **오른쪽 객체를 기준(self)**으로 오버로딩!
            - __rmul__(right multiplication) 특별 메쏘드:
                - *연산자 **오른쪽에 등장하는 객체가 self**가 되고 **왼쪽에 등장하는 객체가 other**.
                - 이 경우에 self와 other의 타입이 달라도 됨.
                ```py
                def __rmul__(self, other):
                    return Point(self.x * other, self.y * other)

                r = 3 * p   # r = p.__rmul(3)의 형식으로 호출됨(반대가 되면 안 됨!) 
                ```
           
        ```py
        class Point:
            def __init__(self, x=0, y=0):
                self.x = x
                self.y = y

            def __str__(self):
                return f"({self.x}, {self.y})"

            def __add__(self, other):
                return Point(self.x + other.x, self.y + other.y)

            def __sub__(self, other):
                return Point(self.x - other.x, self.y - other.y)

            def __rmul__(self, other):
                return Point(self.x * other, self.y * other)

        p = Point(1, 2)
        q = Point(3, 4)
        r = p - q
        print(r)
        r = 3 * p
        print(r)
        r= p * 3    # 에러 발생 -> 오른쪽에 벡터가 와야하고 왼쪽에 스칼라가 와야함! 
        print(r)    # __rmul__이 오른쪽 객체를 기준으로 오버로딩하기 때문!
        ```