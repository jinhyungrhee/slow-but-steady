# 큰 수의 법칙 문제
# 연속으로 더할 수 있는 횟수는 최대 K번이므로, '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복!

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

result = 0

while True:
  # 가장 큰 수를 k번 더함
  for i in range(k):
    # m이 0이면 반복문 탈출
    if m == 0:
      break
    result += first
    # 더할 때마다 1씩 횟수 차감
    m -= 1
  
  # m이 0이면 반복문 탈출
  if m == 0:
    break
  result += second
  # 더할 때마다 1씩 횟수 차감
  m -= 1

print(result)

'''
문제 : M의 크기가 100억 이상으로 매우 커진다면, 시간 초과 판정이 나올 수 있음
해결 : '반복되는 수열의 길이와 횟수'를 파악하어 계산 복잡도를 줄일 수 있음 
'''