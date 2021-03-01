# a^n을 계산하여 리턴하는 함수

import sys
import timeit

def slow_power(a, n): 
    if n == 1: return a
    return a * slow_power(a, n-1) # (3, 4)이면 3 * s_p(3, 3) * s_p(3, 2) * s_p(3, 1) 
                                  #          = 3 * 3 * 3 * s_p(3, 1) = 3^4

def fast_power(a, n): # a**n = a**n/2 * a**n/2 = a**(n/2) ** 2
    if n == 1: return a
    elif n % 2 == 0: # 짝수
        return fast_power(a, n/2) ** 2
    else: # 홀수
        return a * fast_power(a, n-1)


a = int(input())
n = int(input()) # a와 n을 차례로 입력 받음
start = timeit.default_timer()
slow_power(a, n)
mid = timeit.default_timer()
fast_power(a, n)
end = timeit.default_timer()
print("{}, {}".format(start-mid, mid-end))
