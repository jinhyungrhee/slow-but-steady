# 순차 탐색
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

print("생성할 원소 개수와 찾을 문자열을 입력하시오.(공백으로 구분)")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("지정한 개수 만큼의 문자열을 입력하시오.(공백으로 구분)")
array = input().split() # 리스트로 저장됨

print(sequential_search(n, target, array))

