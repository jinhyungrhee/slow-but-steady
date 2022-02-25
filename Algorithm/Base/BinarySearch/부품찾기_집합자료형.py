''' <집합 자료형>
단순히 특정한 데이터가 존재하는지 검사할 때 매우 유용한 방법
set() : 집합 자료형을 초기화할 때 사용
'''

n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split())) # {2, 3, 7, 8, 9}

m = int(input())
# 손님이 요청한 부품
req = list(map(int, input().split()))

# 확인
for elem in req:
  if elem in array:
    print("yes", end=" ")
  else:
    print("no", end=" ")