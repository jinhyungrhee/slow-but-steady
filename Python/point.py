import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def length(self): # 길이(sqrt(x^2+y^2))
        return math.sqrt(self.x**2 + self.y**2) # sqrt : 제곱근 함수

    def dot(self, q): # 내적(= p.x*q.x + p.y*q.y)
        return self.x*q.x + self.y*q.y

    def dist(self, q): # 거리(length(p-q))
        return (self-q).length()

    def move(self, dx=0, dy=0): # 이동(점 p를 x-축으로 dx만큼, y-축으로 dy만큼 더해 이동)
        self.x += dx
        self.y += dy
    '''
     점의 좌표 값 읽거나 변경 => p.x, p.y처럼 멤버 값을 직접 참조 하는 것은 객체지향언어 원칙에 위배!
                             => 최대한 클래스 내부의 멤버 값을 직접 참조하지 않고 정해진 메쏘드로만 참조!
    '''
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get(self):
        return f"({self.x}, {self.y})"

    def setX(self, val):
        self.x = val

    def setY(self, val):
        self.y = val

    def set(self, val1, val2):
        self.x, self.y = val1, val2


p = Point(1, 2)
q = Point(2, 3)
print(f"p = {p}, q = {q}") # p = (1, 2), q = (2, 3)
print("length of p =", p.length()) # 2.23606797749979
print("length of q =", q.length()) # 3.60555127543989
print("dot of p and q =", p.dot(q)) # 8
print("dist of p and q =", p.dist(q)) # 1.4142135623730951
p.move(3, 5)
print("move p by (3, 5) =", p) # (4, 7)
p.setX(2)
print(p.get()) # (2, 7)
p.setY(9)
print(p.get()) # (2, 9)
p.set(6, 1)
print(p.getX()) # 6
print(p.getY()) # 1