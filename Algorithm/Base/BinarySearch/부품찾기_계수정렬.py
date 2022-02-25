''' <계수정렬>
모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤,
리스트의 인덱스에 접근하여 특정 번호의 부품이 가게에 존재하는지 확인
'''

n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호 입력받아 기록
# 인덱스가 부품 종류, 값이 부품 존재 유무(1-유, 0-무)
for i in input().split():
  array[int(i)] = 1

m = int(input())
# 손님 요청 부품
req = list(map(int, input().split()))

for elem in req:
  # 가게에 존재하는 지 확인
  if array[elem] == 1:
    print('yes', end=" ")
  else:
    print('no', end=" ")