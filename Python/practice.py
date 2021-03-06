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

