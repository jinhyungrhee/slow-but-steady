array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  # 이번 라운드에서 가장 작은 원소의 인덱스 찾아서 swap
  array[i], array[min_index] = array[min_index], array[i]

print(array)
