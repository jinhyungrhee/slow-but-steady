# 두 개의 최소 신장 트리 생성(크루스칼 알고리즘)
# 최소 신장 트리를 찾은 후, 최소 신장 트리를 구성하는 간선 중 가장 비용이 큰 간선 제거
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())

# 부모 리스트 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수 선언 **
edges = []
result = 0

for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b)) # 비용순으로 정렬하기 위해

# 간선을 비용순으로 정렬
edges.sort()
# 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선 **
last = 0

for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost # 최종 비용
    last = cost # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 것 기록

print(result - last) # 최소 신장 트리를 구성하는 간선 중 가장 비용이 큰 간선 제거

'''
(입력)
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
(출력)
8
'''