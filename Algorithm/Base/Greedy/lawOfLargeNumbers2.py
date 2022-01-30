# 큰 수의 법칙 계산 복잡도 줄이기

'''
반복되는 수열의 길이 : (K + 1)
수열이 반복되는 횟수 : M / (K + 1)
가장 큰 수가 더해지는 횟수 : int(M / (K + 1)) * K + M % (K + 1)
'''

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기 - 리스트 생성
data = list(map(int, input().split()))

# 입력받은 수들 정렬
data.sort()
# 가장 큰 수
first = data[n - 1]
# 두번째로 큰 수
second = data[n - 2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k # int(A / B) == A//B
count += m % (k + 1) # M이 (K + 1)로 나누어떨어지지 않는 경우도 고려

result = 0
# 가장 큰 수 더하기
result += (count) * first
# 두 번째로 큰 수 더하기
result += (m - count) * second

print(result)