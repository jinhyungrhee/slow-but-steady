'''
21.03.19 실습 수업 내용
'''

import math

class Point:
    def __init__(self, x=0, y=0): # 생성함수 -> 포인트 클래스가 obj를 생성할 때 가장 먼저 호출(무조건 한번은 실행)
        self.x = x  # self -> 자기 자신 객체. 내 안의 뭔가를 찾고 싶을 때 "."을
        self.y = y

    def __str__(self): # 내가 쓰고 싶어서 호출하는 것이 아니라 python 인터프리터에서 알아서 호출해줌 - 내가 string형으로 보고 싶을 때 알아서 호출
        return f"({self.x}, {self.y})"

    def __add__(self, other): # 매직매서드 정의해서 더하기 연산 가능해짐!! 파이썬 자체의 기능을 쓰고 싶을 때 정의 - 내가 더하기 연산을 하고 싶을 때 파이썬이 알아서 호출
        return Point(self.x + other.x, self.y + other.y) 

    def f(self):
            print('HI')

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def getX(self):
        return self.x

def errormsg():
    print('error')

'''
p = a + b 
p = a.__add___(b) # self = a(호출한 자기 자신) , other = b(두번째로 오는 인자) // 왼쪽에 등장하는 애가 self가 됨
'''
    
'''
p = Point(1, 2)
q = Point(3, 5)
r = p + q 
p.f()
print(p)
print(r)
'''

'''
p = Point()

p[0] # __getitem__ 사용

p[0] = 1 # __setitem__ 사용
p.__setitem__(0, 1) # 파이썬이 이런식으로 해석
'''
print(errormsg())