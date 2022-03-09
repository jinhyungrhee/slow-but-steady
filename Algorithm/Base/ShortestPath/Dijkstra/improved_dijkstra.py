'''
* 개선된 다익스트라 알고리즘 *
- 힙(Heap) 자료구조 사용 : 특정 노드까지의 최단 거리에 대한 정보 저장 -> 더 빠르게 찾기 가능!(선형 시간이 아닌 로그 시간)
- 최단 거리를 저장하기 위한 1차원 리스트(= 최단 거리 테이블)는 그대로 사용하고, 현재 가장 가까운 노드를 저장하기 위한 목적으로 '우선순위 큐' 사용!
- get_smallest_node() 함수 대신 '우선순위 큐'를 사용하여 다익스트라 함수 안에서 최단 거리가 가장 짧은 노드를 선택

시간복잡도 : O(ElogV) (V는 노드의 개수, E는 간선의 개수)
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# '각 노드에 연결된 노드 정보'를 담은 리스트 생성
graph = [[] for i in range(n + 1)]
# '최단 거리 테이블'을 모두 무한으로 초기화
distance = [INF] * (n + 1)
# visited 리스트는 필요X

# 간선 정보 입력
for _ in range(m):
  # a노드에서 b노드로 가는 비용이 c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로를 0으로 하여 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  # 큐가 빌 때까지 반복 (-> 노드 개수 V이상의 횟수로는 반복되지 않음!) **
  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면(=이미 최단거리로 갱신되었다면) 무시 **
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접 노드 확인 (->총 최대 간선 개수 E만큼 연산 수행)**
    for i in graph[now]:
      cost = dist + i[1] # i[1] : b노드로 가는 비용(c)
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost # 최단 거리 갱신
        heapq.heappush(q, (cost, i[0])) # i[0] : 인접노드(b)

# 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
  # 도달할 수 없는 경우
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
