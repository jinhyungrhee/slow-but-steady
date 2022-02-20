# 파이썬의 장점을 살린 퀵 정렬 

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만 담고 있다면 종료
  if len(array) <= 1:
    return array # 주의) 함수 종료 시 array를 반환해야 함!

  pivot = array[0] # 첫번째 원소가 피벗
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

  # 분할 이후 왼쪽 부분과 오른쪽 부분에 대해 재귀적으로 정렬을 수행하고 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

'''
장점 : 전통적인 퀵 정렬보다 더 직관적이고 기억하기 쉬움
단점 : 전통적인 퀵 정렬에 비해 비효율적
'''