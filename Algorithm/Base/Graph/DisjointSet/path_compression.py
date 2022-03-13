'''
경로 압축(Path Compression): find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신하는 기법
'''
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # find 재귀 호출 뒤 부모 테이블 갱신(해당 루트노드가 바로 부모노드가 됨)
  return parent[x]