array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 두 번째 데이터부터 시작
for i in range(1, len(array)):
  for j in range(i, 0, -1): # i부터 1까지 감소하면서 비교
    if array[j] < array[j - 1]: # 앞의 원소가 더 크면 swap
      array[j] , array[j - 1] = array[j - 1], array[j]
    else: # 뒤의 원소가 더 크면 멈춤
      break

print(array)

