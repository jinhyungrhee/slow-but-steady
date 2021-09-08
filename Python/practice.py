'''
# ex1-최대값과 최소값 구하는 함수

from functools import reduce
A = list(map(int, input().split()))
min_max = reduce(lambda x, y: x if x < y else y, A), reduce(lambda x, y: x if x > y else y, A)
print(min_max)


# ex2-소수인지 판별하는 함수

def is_prime(x):
    for i in range(2, x): # 2부터 x-1까지 모든 수를 확인
        if x % i == 0:    # ex) 5의 경우 -> 5를 2, 3, 4로 나눠서 하나라도 나머지가 0이면 False, 나머지가 0이 아니면 True
            return False
    return True

p = int(input())
print(is_prime(p))

# ex4-정수 x의 각 자리수의 합을 str,map,sum함수를 이용하여 한 줄 코드로 작성

#hint
def sum_digit(number):
    result = 0
    for i in str(number):
        result = result + int(i)
    return result

print("결과 : {}".format(sum_digit(input())))
'''
'''
A = sum(map(lambda x: for x in str(input())))
print(A)
'''

'''
# 최대공약수 알고리즘(Euclid, 최초의 알고리즘) -> gcd_sub, gcd_mod, gcd_rec

def gcd_sub(a, b): # 큰 수에 작은 수를 뺀 '나머지'로 최대공약수를 구하는 방법
    while a != 0 and b != 0:
        if a > b: a -= b
        else: b -= a 
    return a + b # a 또는 b를 리턴! (둘 중 하나는 0)

def gcd_mod(a, b): # 큰 수에 작은 수를 나눈 '나머지'로 최대공약수를 구하는 방법 -> 많은 연산을 건너 뜀!
    while a != 0 and b != 0:
        if a > b: a %= b
        else: b %= a
    return a + b

# 재귀호출로 최대공약수 구하는 함수
def gcd_rec(a, b): # gcd_sub(90, 40) = gcd_sub(90-40, 40) = gcd_sub(큰값-작은값, 작은값) = ... = gcd_sub(큰값-작은값, 0) = 10
    if a*b == 0: return a + b
    if b > a: a, b = b, a # b가 a보다 크면 a와 b의 위치 변경
    return gcd_rec(a-b, b)


# a,b 크기 비교 없이, 절대값(abs)을 이용하면 안 될까?
def gcd_rec_abs(a, b):
    if a*b == 0: return a + b
    return gcd_rec_abs(abs(a-b), b)

# => RecursionError 발생! : 90-40 = 50-40 = 10-40 = 30-40 = 10-40 = 30-40 = ... 무한히 반복되어 maxmimum recursion depth를 초과함!


a, b = map(int, input().split())
x, y, z = gcd_sub(a, b), gcd_mod(a, b), gcd_rec(a, b)
print(x, y, z)

'''
class myList():
    def __init__(self): 
        self.capacity = 2   # myList의 용량 (저장할 수 있는 원소 개수)
        self.n = 0          # 실제 저장된 값의 개수
        self.A = [None] * self.capacity # 실제 저장 자료 구조(Python리스트)

    def __len__(self):
        return self.n

    def __str__(self):
        return f'   ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

    def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if k < 0 and k >= -(self.n):
            return self.A[self.n + k]
        elif k >= 0 and k < self.n:
            return self.A[k]
        else:
            raise IndexError


    def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if k < 0 and k >= -(self.n):
            self.A[self.n + k] = x
        elif k >= 0 and k < self.n:
            self.A[k] = x
        else:
            raise IndexError

    def change_size(self, new_capacity):
	    #print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
	    # 1. new_capacity의 크기의 리스트 B를 만듬
	    # 2. self.A의 값을 B로 옮김
	    # 3. del self.A  (A 지움)
	    # 4. self.A = B
	    # 5. self.capacity = new_capacity
        B = [None] * new_capacity # new_capacity = 5이면,  [None, None, None, None, None]
        for i in range(self.capacity): #self.A의 원소 B로 옮김
            B[i] = self.A[i]
        self.A.clear()
        self.A = B
        self.capacity = new_capacity

    def append(self, x):
        if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
            self.change_size(self.capacity*2)
            self.A[self.n] = x      # 맨 뒤에 삽입
            self.n += 1             # n 값 1 증가   
        else:
            self.A[self.n] = x      # 맨 뒤에 삽입
            self.n += 1             # n 값 1 증가

    def insert(self, k, x):
        # 주의 : k 값이 음수값일 수도 있음
        # k 값이 올바른 인덱스 범위를 벗어나면 , raise IndexError
        # 1. k의 범위가 올바르지 않다면 IndexError 발생시킴
        # 2. self.n == self.capacity이면 self.changing_size(self.capacity*2) 호출해 doubling
        # 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
        # 4. self.A[k] = x
        # 5. self.n += 1
        if k < 0 and k >= -(self.n): # k값이 음수일 때
            if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
                self.change_size(self.capacity*2)
            for i in range(self.n-1, self.n+k-1, -1): # k = -2이면
                self.A[i+1] = self.A[i]
            self.A[self.n+k] = x
            self.n += 1
        elif k >= 0 and k < self.n: # k가 인덱스를 벗어나지 않는 양수일때
            if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
                self.change_size(self.capacity*2)
            for i in range(self.n-1, k-1, -1):
                self.A[i+1] = self.A[i]
            self.A[k] = x
            self.n += 1
        else:
            raise IndexError

    def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
        if self.n == 0: # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: (음수도 처리해줘야함..ㅠㅠ)
            raise IndexError
        elif self.capacity >= 4 and self.n <= self.capacity//4 : # 실제 key값이 전체의 25%이하면 halving
            self.change_size(self.capacity//2)
        # 1. k값이 주어진 경우와 주어지지 않은 경우를 구별해야 함
        # 2. x = self.A[k]
        # 3. A[k]와 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
        # 4. self.n -= 1
        # 5. return x
        if k == None:
            x = self.A[self.n-1]
            self.A[self.n-1] = None
            self.n -= 1
            return x
        elif k >= 0 and k < self.n:
            x = self.A[k] 
            self.A[k] = None
            for i in range(k, self.n-1): # A[k]와 오른쪽 값들이 한 칸씩 왼쪽으로 이동해 메꿈
                self.A[i] = self.A[i+1]
            self.n -= 1
            return x
        elif k < 0 and k >= -(self.n):
            x = self.A[self.n + k] # 여기가 문제
            self.A[self.n + k] = None
            for i in range(self.n+k, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
            return x
        else:
            raise IndexError



L =myList()
'''
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.append(6)
L.append(7)

print(L)
# __getitem__ 선언했으므로 L[5] 이렇게만 해도 알아서 getitem호출함 ***
print(L[-3]) # 인덱스 값 벗어남 => 인덱스 에러 발생시켜야함 => ok 완료! = 이렇게 발생시키기만 하면 실행문에서 try except로 잡을것임!
#print(L.n)  # 실제 저장된 값의 개수 = 5
#L.__setitem__(-3, 7)
#print(L.n)
#print(L)

# ** 여기까지 완벽 **

print(L)
L.insert(6, -1)
print(L)
L.insert(-8, 17)
print(L)

# 좀 애매하지만 일단 맞다고 생각하고 진행하자 insert(음수, value) 살짝 애매함

print(L.pop())
print(L)
'''
L.append(0)
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
print(L)
L.insert(-2, -3)
print(L)
L.insert(-7, 9)
print(L)
L.insert(-8, -9)
print(L)