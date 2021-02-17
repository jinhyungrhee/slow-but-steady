- ### 연산자 오버로딩(Overloading)
    - 정수, 실수 덧셈처럼 ``` r = p + q ```의 형식으로 **+** 연산자를 사용할 수 있다면 직관적이고 더 이해하기 쉬움. 파이썬에서는 이를 위한 특별 메쏘드(```__add__```)를 제공함.
    - 정수, 실수의 덧셈 **+** 연산자에 Point 클래스의 덧셈 연산을 **덧입혔다**는 의미에서 이를 "**연산자 overloading**"이라고 함.
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
        - ```__add__``` : ```+```
        - ```__sub__``` : ```-```
        - ```__mul__``` : ```*```
        - ```__truediv__``` : ```/```
        - ```__floordiv__``` : ```//```
        - ```__mod__``` : ```%```
        - ```__iadd__``` : ```+=```
        - ```__isub__``` : ```-=```
        - ```__imul__``` : ```*=```
        - ```__itruediv__``` : ```/=```
        - ```__ifloordiv__``` : ```//=```
        - ```__imod__```: ```%=```
        
    - 비교 연산자 오버로딩:
        - ```__lt__``` : ```<```
        - ```__le__``` : ```<=```
        - ```__gt__``` : ```>```
        - ```__ge__``` : ```>=```
        - ```__eq__``` : ```==```
        - ```__ne__``` : ```!=```

    - 서로 다른 타입의 객체끼리 연산
        - **scalar * vector 형식** : ```r = 3 * p```처럼 p의 좌표 값에 모두 상수 3을 곱하는 식으로 사용됨
        - scalar 값은 Point 객체가 아니기 때문에 **연산에 참여하는 두 객체의 타입이 같지 않다**는 문제 발생.
        - 이러한 경우에도 연산자 오버로딩 기능 지원. 단 **오른쪽 객체를 기준(self)**으로 오버로딩!
            - ```__rmul__```(right multiplication) 특별 메쏘드:
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