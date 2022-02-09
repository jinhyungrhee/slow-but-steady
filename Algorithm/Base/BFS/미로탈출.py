from collections import deque

n, m = map(int, input().split())

graph = [
  list(map(int, input()))
  for _ in range(n)
]

# dx-dy테크닉 : 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 구현
def bfs(x, y):
  # '큐' 구현을 위한 deqeu 라이브러리 사용
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재의 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간을 벗어난 경우 무시
      if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n - 1][m - 1]

# bfs 호출
print(bfs(0, 0))