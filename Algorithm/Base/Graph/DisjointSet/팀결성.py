# '같은 팀 여부 확인' 연산 
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# '팀 합치기' 연산
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, m = map(int, input().split())

# 부모리스트 초기화
parent = [0] * (n + 1)

for i in range(1, n+1):
  parent[i] = i

# 입력 받기
for _ in range(m):
  # a와 b는 n 이하의 양의 정수
  type, a, b = map(int, input().split())

  if type == 0: # 팀 합치기 연산 수행
    union_parent(parent, a, b)
  else: # 같은 팀 여부 확인 연산 수행
    if find_parent(parent, a) == find_parent(parent, b):
      print('YES')
    else:
      print('NO')


'''
(입력조건)
'팀 합치기' 연산은 0 a b 형태로 주어짐
'같은 팀 여부 확인'연산은 1 a b 형태로 주어짐
a와 b는 N이하의 양의 정수임
(입력)
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
(출력)
NO
NO
YES
'''