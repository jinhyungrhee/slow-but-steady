# 서로소 집합 활용 => '무방향 그래프'에서만 가능!
# (DFS 활용 - 방향 그래프)

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(=union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블 상에서, 자기 자신을 부모로 초기화
for i in range(1, v+1):
  parent[i] = i

# 사이클 발생 여부 플래그 **
cycle = False

for i in range(e):
  a, b = map(int, input().split())
  # 사이클이 발생한 경우 종료
  if find_parent(parent, a) == find_parent(parent, b): # 두 노드가 동일한 루트 노드를 가지고 있으면 Cycle 발생!
    cycle = True
    break
  # 사이클이 발생하지 않았으면 union 연산 수행
  else:
    union_parent(parent, a, b)

# 출력
if cycle:
  print("사이클이 존재합니다.")
else:
  print("사이클이 존재하지 않습니다.")