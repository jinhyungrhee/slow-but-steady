# 점화식 : Ai = min(Ai-1, Ai/2, Ai/3, Ai/5) + 1 
# -> 함수의 호출 횟수를 구해야 하기 때문에 마지막에 1 더해줌!
# -> (i-1) 연산을 제외하고 해당 수로 나누어 떨어질 때에 한해서만 점화식 적용 가능

x = int(input()) # 26

# DP 테이블 초기화
d = [0] * 30001

# DP 진행(바텀업 방식 - 단순 반복문)
for i in range(2, x + 1): # 2 ~ 26
  # 현재 수에서 1 뺀 경우는 비교 없이 그냥 저장
  d[i] = d[i - 1] + 1
  
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1) # 방금 저장한 값과 나누기 2 연산을 한 값 + 1 중 더 작은 값으로 저장

  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)  # 방금 저장한 값과 나누기 3 연산을 한 값 + 1 중 더 작은 값으로 저장

  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)  # 방금 저장한 값과 나누기 5 연산을 한 값 + 1 중 더 작은 값으로 저장
  
  # 작은 숫자들부터 각 최소 연산횟수가 DP 테이블에 저장되어 있으므로 그대로 가져다 사용 가능!

print(d[x])

''' 그냥 재귀 => 최소횟수 출력X
def make_one(n, cnt):

  # 종료 조건
  if n == 1:
    return cnt

  if n % 5 == 0:
    return make_one(n/5, cnt + 1)
  elif n % 3 == 0:
    return make_one(n/3, cnt + 1)
  elif n % 2 == 0:
    return make_one(n/2, cnt + 1)
  else:
    return make_one(n - 1, cnt + 1)

print(make_one(26, 0))
'''