# 이진탐색(재귀 함수)
def binary_search(array, target, start, end):
  
  if start > end: # 종료 조건
    return None
  
  mid = (start + end) // 2 # 중간점
  
  # 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  # 중간점 값보다 찾고자 하는 값이 작은 경우 -> 왼쪽 확인 (end = mid - 1)
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  # 중간점 값보다 찾고자 하는 값이 큰 경우 -> 오른쪽 확인(start = mid + 1)
  else:
    return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split())) # 각각 따로 저장됨

array = list(map(int, input().split())) # array에 한꺼번에 저장됨

# 이진 탐색 수행
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)