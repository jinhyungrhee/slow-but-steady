# 경로 압축(Path Compression) 기법을 사용하면 루트 노드에 더 빠르게 접근할 수 있으므로 시간복잡도가 개선됨!

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트노드가 아니면, 루트 노드 찾을 때까지 재귀 호출(=**경로 압축**)
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # 부모 테이블에 부모 노드 대신 루트 노드가 저장됨
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

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

# union 연산 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
  print(parent[i], end=' ')


'''
(입력)
6 4
1 4
2 3
2 4
5 6
(출력)
각 원소가 속한 집합:  1 1 1 1 5 5 
부모 테이블:  1 1 1 1 5 5 # # 부모 테이블에 부모 노드 대신 루트 노드가 저장됨(=> *경로 압축*)

# 시간복잡도 : 노드 개수가 V이고, 최대 V-1개의 union 연산과 M개의 find 연산이 가능할 때, O(V + M * (1 + log2-m/vV))
'''