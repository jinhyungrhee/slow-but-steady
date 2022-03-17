# N개의 강의에 대하여 수강하기까지 걸리는 최소시간을 각각 출력
from collections import deque
import copy

v = int(input())

indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
# 각 강의시간
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0] # 첫번째 데이터는 소요시간(time 리스트로 관린)
  for x in data[1:-1]: # (맨 마지막 데이터는 -1이므로 제외)
    indegree[i] += 1   # i노드로 들어오는 간선의 개수(=진입차수) 1증가
    graph[x].append(i) # x노드에서 i노드로 갈 수 있음

# 위상정렬
def topology_sort():
  result = copy.deepcopy(time) # time 리스트 깊은 복사
  q = deque()

  # 처음 시작 시 진입차수가 0인 노드들만 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 빌 때까지 반복
  while q:
    now = q.popleft()
    for i in graph[now]:
      # 인접한 노드에 대하여 현재보다 강의 시간이 더 긴 경우를 찾는다면,
      # 더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블을 갱신 **
      result[i] = max(result[i], result[now]+time[i])
      # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 위상 정렬을 수행한 결과 출력
  for i in range(1, v+1):
    print(result[i])

topology_sort()

'''
(입력)
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
(출력)
10
20
14
18
17
'''