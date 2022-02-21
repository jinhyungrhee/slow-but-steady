n = int(input())

# n개의 정수를 입력받아 리스트에 저장
data = []
for _ in range(n):
  data.append(int(input()))

# 파이썬 기본 정렬 라이브러리 이용하여 정렬 수행
data.sort(reverse = True)

# 출력
for elem in data:
  print(elem, end=' ')