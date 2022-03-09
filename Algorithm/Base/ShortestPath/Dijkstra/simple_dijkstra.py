'''
* 단순한 다익스트라 알고리즘 *
1)처음에 각 노드에 대한 최단 거리를 담은 1차원 리스트를 선언
2)이후 단계마다 '방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택'하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차탐색)

시간 복잡도 : O(V^2) (V는 노드의 개수)
=> 전체 노드 수가 5,000개 이하인 문제는 통과 가능하지만, 10,000개가 넘어가는 문제는 해결하기 어려움
'''

import sys
input = sys.stdin.readline
INF = int(1e9) 

# 노드 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# '각 노드에 연결된 노드 정보'를 담은 리스트 생성
graph = [[] for i in range(n + 1)]
# '이미 방문한 노드 정보'를 담은 리스트 생성
visited = [False] * (n + 1)
# '최단 거리 테이블'을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 간선 정보 입력받기
for _ in range(m):
  # a노드에서 b노드로 가는 비용이 c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 최단 거리가 짧은 노드의 인덱스
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드에 대해서 초기화
  distance[start] = 0 # 시작노드의 거리는 0
  visited[start] = True # 방문 체크
  # 시작 위치에서 갈 수 있는 노드의 '최단 거리 테이블' 갱신 (아직 방문 X)
  for j in graph[start]: 
    distance[j[0]] = j[1]

  # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
  for i in range(n - 1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost # 더 짧은 거리로 갱신

# 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
  # 도달할 수 없는 경우
  if distance[i] == INF:
    print("INFINITY")
  # 도달 가능한 경우
  else:
    print(distance[i])