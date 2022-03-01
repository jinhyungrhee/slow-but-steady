# 금액 i를 만들 수 있는 최소한의 화폐 개수를 Ai, 화폐 단위를 k라고 할 때,
# 점화식: (Ai-k는 금액 (i-k)를 만들 수 있는 최소한의 화폐 개수)
# (1) Ai-k를 만드는 방법이 존재하는 경우, Ai = min(Ai, Ai-k + 1)
# (2) Ai-k를 만드는 방법이 존재하지 않는 경우, Ai = 10001

# TIP : k의 크기만큼의 리스트 할당, 이후 각 인덱스를 '금액'으로 고려하여 메모이제이션 진행!

n, m = map(int, input().split()) # 3 7

# array = list(map(int, input().split()))
array = []
for _ in range(n):
  array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n): # 0 1 2 
  for j in range(array[i], m + 1): # 2 ~ 8, 3 ~ 8, 5 ~ 8
    if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하면 (-> 없어도 ok)
      d[j] =  min(d[j], d[j - array[i]] + 1)

# 출력
if d[m] == 10001: # 최종적으로 m원을 만드는 방법이 없음
  print(-1)
else:
  print(d[m])