# 계수 정렬(비교 기반 정렬 알고리즘X)

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

# 출력
for i in range(len(count)):
  for j in range(count[i]): # 만약 원소 i가 존재하지 않으면 for문이 돌지 않으므로 출력X
    print(i, end=" ")
