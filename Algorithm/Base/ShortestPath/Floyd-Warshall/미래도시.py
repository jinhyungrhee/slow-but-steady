INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 간선 정보
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())
  
# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1부터 k도시를 들른 뒤, k도시에서 x도시로 가는 최단 경로
dist = graph[1][k] + graph[k][x]

if dist >= INF:
  print(-1)
else:
  print(dist)