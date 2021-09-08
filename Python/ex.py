import random, time

def unique_n(A): # A의 값들이 "-n부터 n사이의 값들"이라는 정보 이용 -> 새로운 리스트 B를 정의해 이용하는 방법! ->O(n) 시간에 동작하는 알고리즘
    B = [0 for i in range(n*2+1)] # A = [-5, 2, -3, 0, 1] -> 이것을 B의 인덱스로 활용
    for i in range(0, n):
        tmp = A[i] + n
        if B[tmp] == 0:
            B[tmp] = 1
        else: return 'NO'
    return 'YES'
        
def unique_nlogn(A): # sort() -> n개 값을 O(nlogn)에 정리. 단일 for 루프 사용!
    A.sort() # n개의 값을 O(nlogn)시간에 정렬
    for i in range(0, n-1):
        if A[i] == A[i+1]: # 오름차순을 만들면, 연속된 값이 다르다면 전부 다른 값임을 유추할 수 있음!
            return 'NO'
    return 'YES'

def unique_n2(A): # 이중 for 루프 사용 => O(n^2)
    for i in range(0, n): # n번
        for j in range(i+1, n): # n번
            if A[i] == A[j]:
                return 'NO'
    return 'YES'

# input: 값의 개수 n
n = int(input())
# -n과 n 사이의 서로 다른 값 n개를 랜덤 선택해 A구성
A = random.sample(range(-n, n+1), n)

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
# 동시에 각 함수의 실행 시간을 측정해본다
# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다


# A의 값들이 '-n부터 n사이의 값들'이라는 정보 이용 -> n을 이용하라는 것인가?
# 새로운 리스트 B를 정의해 이용하는 방법! -> B에 집어넣는데 중복되는 값이 있으면 표현안됨! ***
# O(n) 시간에 동작하는 알고리즘

''''
n=5
C = [-1, 2, -1, -4, -3] # n = 5 (-5부터 5 사이의 값들) -> 2 중복!
B = [0 for i in range(n*2+1)] # 새로운 리스트B 이용
for i in range(0, n):
    if B[C[i] + n] == 0:
        B[C[i] + n] = 1
    else: print("NO")  # 4, 7, 2, 1, 7 -> B[4] = -1, B[7] = 2, B[2] = -3, B[1] = -4 , B[7] = 2
print("YES")
'''


'''
n = 5
A = [5, 2, 3, -4, 0]

print(unique_n(A))
print(unique_n2(A))
print(unique_nlogn(A))

'''

s = time.perf_counter()
unique_n(A)
e = time.perf_counter()
print("n수행시간 =", e-s)


s3 = time.perf_counter()
unique_nlogn(A)
e3 = time.perf_counter()
print("nlogn수행시간 =", e3-s3)
'''
s2 = time.perf_counter()
unique_n2(A)
e2 = time.perf_counter()
print("n^2수행시간 =", e2-s2)
'''
