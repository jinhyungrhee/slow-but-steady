# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트노드가 아니면, 루트노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(= union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 맨 처음 부모를 자기 자신으로 초기화(부모 테이블 초기 갱신)
for i in range(1, v+1):
  parent[i] = i

# union 연산 각각 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 각 원소가 속합 집합 출력
print('각 원소가 속합 집합: ', end='')
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
각 원소가 속합 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 2 1 5 5 # 부모 테이블에 부모 노드가 저장됨(루트 노드X)

# find_parent 함수가 최악의 경우 O(V)로 동작함 => 비효율적!
# 4개의 union 연산 : (4, 5), (3, 4), (2, 3), (1, 2)인 경우, 노드 5의 루트를 찾기 위해 '5->4->3->2->1' 순서대로 거슬러 올라감
# 만약 노드의 개수가 V개이고 find 또는 union 연산의 개수가 M일 때, 전체 시간복잡도는 O(VM)이 됨
# ** 경로 압축(Path Compression) 기법을 통해 시간복잡도 개선 가능 ** 
'''