
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

