# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀 호출
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
parent = [0] * (v+1)  # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 '비용'으로 설정
  edges.append((cost, a, b))

# 간선을 '비용'순으로 오름차순 정렬
edges.sort()

# 간선을 하나씩 확인
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)


'''
(입력)
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
(출력)
159
'''