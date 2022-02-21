# 1 <= n <= 100,000 이면 O(n^2) 알고리즘은 불가
# 따라서 기본 정렬 라이브러리(O(nlogn))나 계수정렬(O(n)) 사용!

n = int(input())

data = []
for _ in range(n):
  input_data = input().split()
  data.append((input_data[0], int(input_data[1])))


# key 매개변수 사용하여 정렬(두 번째 원소 기준)
data.sort(key=lambda student : student[1])

# 출력
for elem in data:
  print(elem[0], end=' ')