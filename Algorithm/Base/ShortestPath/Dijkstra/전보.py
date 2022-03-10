import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

# 도시 개수(n + 1개)만큼의 빈 이차원 리스트 생성
graph = [[] for _ in range(n + 1)]
# '최단 거리 정보' 리스트
distance = [INF] * (n + 1)

# 노드와 간선 입력받기 (그래프)
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))


def dijkstra(start): # 1부터 시작 (start = 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q: # 큐가 빌 때까지(최소 거리가 가장 작은 것이 위로 올라옴)
    dist, now = heapq.heappop(q)
    # 이미 처리된 적 있는 노드(=INF값이 아닌 노드)는 무시 ** 
    if distance[now] < dist: 
      continue
    # 그래프에서 인접 노드 확인
    for i in graph[now]:
      cost = dist + i[1] # 현재 노드의 비용(=최소 거리값)과 인접 노드의 비용 더한 값("새로운 거리값")
      if cost < distance[i[0]]: # "새로운 거리값"이 인접 노드의 '최단 거리 정보' 리스트 값보다 작으면 갱신
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(start)

cnt = 0
# 도달할 수 있는 노드 중, 가장 멀리 있는 노드와의 최단 거리
max_dist = 0 
for i in distance:
  if i != INF:
    max_dist = max(max_dist, i)
    cnt += 1

print(cnt - 1, max_dist) # 시작 노드는 제외(cnt - 1)