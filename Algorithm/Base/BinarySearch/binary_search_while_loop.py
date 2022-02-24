# 이진 탐색(반복문)
def binary_search(array, target, start, end):
  
  while start <= end: # start가 end보다 커지면(=어긋나면) 종료
    
    mid = (start + end) // 2 # 중간점

    # 찾은 경우 인덱스 반환
    if array[mid] == target:
      return mid
    # 중간점 값보다 찾고자 하는 값이 작은 경우 -> 왼쪽 탐색 (end = mid - 1)
    elif array[mid] > target:
      end = mid -1
    # 중간점 값보다 찾고자 하는 값이 큰 경우 -> 오른쪽 탐색(start = mid + 1)
    else:
      start = mid + 1
    
  # 끝까지 탐색했음에도 값을 못 찾은 경우 None 리턴
  return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

# 이진 탐색 수행
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
