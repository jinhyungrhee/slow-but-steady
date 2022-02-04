# 숫자 카드 게임 - 2중 반복문 구조 사용
'''
조건
1. 숫자가 쓰인 카드들이 N * M 형태로 놓여있다. 이때 N은 행의 개수, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
   최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
'''

n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = 10001
  for a in data:
    min_value = min(a, min_value)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)

# 입력으로 들어오는 수는 모두 10,000 이하이므로 
# 단순히 배열에서 가장 작은 수를 찾는 기본 문법과 가장 큰 수를 찾는 기본 문법을 사용하여 해결 가능!