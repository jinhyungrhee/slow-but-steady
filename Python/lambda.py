# <일반 함수와 비교>

def add1(a, b):
    return a + b

print(add1(2, 3))

add2 = lambda a,b: a+b # add2 -> 함수이름. a,b -> 매개변수, a+b -> 명령문장
print(add2(3, 4)) 


# <y-좌표 값 오름차순 정렬>

a = [(1, 2), (4, 1), (3, 9), (2, 4)]
a.sort(key=lambda x: x[1]) # sort()는 기본적으로 오름차순 정렬. key옵션 사용시 비교할 값(리스트 원소 x의 x[1]값) lambda함수로 반환
print(a) # [(4, 1), (1, 2), (2, 4), (3, 9)]

''' 
a = ['16', '25', '7']
a.sort()
print(a) # ['16', '25', '7'] -> string
a.sort(key=int)
print(a) # ['7', '16', '25'] -> int 
'''

# <lambda + map>
# 제곱
b = list(map(lambda x: x*x, [4, 2, 7]))
print(b)

# 절대값 
a = [-5, 3, -2]
b = list(map(lambda x: -x if x < 0 else x, a))
print(b)
'''
# 한 줄에 여러 개의 정수 값 입력받기(int함수 사용)
a = list(map(int, input().split()))
b = [int(x) for x in input().split()]
print(a)
print(b)
'''
# 두 리스트를 더하기
a = [1, 2, 3]
b = [4 ,5, 6]
add = lambda x, y: x+y
print(list(map(add, a, b))) # [5, 7, 9]

# <lambda + filter>
# 짝수만 모으기
a = [1, 5, 3, 4, 6, 7, 10, 12]
b = list(filter(lambda x: x%2 == 0, a))
print(b)

# <lambda + reduce>
# 리스트의 각 원소 모두 더하기
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4])) # (((1+2)+3)+4) = 10

# 리스트의 최대 원소 값 구하기
from functools import reduce
print(reduce(lambda x,y: x if x > y else y, [1, 3, 6, 2, 8])) 