def binary_search(array, target, start, end):

  while start <= end:

    mid = (start + end) // 2
    
    if array[mid] == target:
      return mid
    elif array[mid] > target: # 왼쪽 탐색
      end = mid - 1
    else: # 오른쪽 탐색
      start = mid + 1

  # 일치하는 것이 없으면 None 리턴
  return None


n = int(input())
stock = list(map(int, input().split()))

m = int(input())
req = list(map(int, input().split()))

stock.sort()

for elem in req:
  result = binary_search(stock, elem, 0, n - 1)
  if result == None:
    print("no", end=" ")
  else:
    print("yes", end=" ")
