from collections import deque

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 '진입차수' 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결리스트(=그래프) 초기화
graph = [[] for i in range(v + 1)] 

# 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) # 정점 a에서 b로 이동 가능
  # '진입차수'(=b로 들어오는 간선의 개수) 1 증가
  indegree[b] += 1

# 위상 정렬 함수
def topological_sort():
  result = [] # 결과를 담을 리스트
  q = deque() # 큐 사용

  # 처음 시작 시, 큐에 '진입차수'가 0인 노드 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌 때까지 반복
  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    # 꺼낸 원소와 연결된 노드들의 '진입차수'에서 1 빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 위상 정렬 결과 출력
  for i in result:
    print(i, end=' ')


topological_sort()


'''
(입력)
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
(출력)
1 2 5 3 6 4 7 
'''