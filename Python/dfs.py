import sys
sys.setrecursionlimit(5000)


def DFS(G, v):  # v노드 방문중! 0 ~ n-1 (노드0부터 차례로 방문)
    global curr_time  # pre, post를 위한 time stamp
    # 그래프 G의 노드 v를 DFS 방문한다
    visited[v] = True  # 노드[v] = 방문 (리스트에 값이 있으면 True?-다 이차원배열로 해야할듯...)
    prev[v] = curr_time
    curr_time += 1
    for w in G[v]:
        if visited[w] == False:  # 인접노드가 아직 방문하지 않은 상태라면
            parent[w] = v
            DFS(G, w)
    # 루프를 다 돌고 나왔다면 v에 인접한 모든 노드 다 고려한 것
    post[v] = curr_time  # v에서 DFS가 완료된 시간 기록(더 이상 v에서 방문할 인접노드가 없을 때)
    curr_time += 1  # time stamp 찍혔으므로 값 하나 증가


def DFSAll(G):
    # 그래프 G를 DFS 방문한다
    for v in range(n):  # 노드 차례로 방문(n = index : 0~n-1)
        if visited[v] == False:
            DFS(G, v)


# 입력 처리
n, m = [int(x) for x in input().split()]  # n:노드, m:에지
G = [[] for _ in range(n)]  # 노드개수만큼 이차원리스트 생성 - 각노드에 연결된 노드들 표시
# G 입력 받아 처리
for i in range(0, m):
    a, b = [int(x) for x in input().split()]
    G[a].append(b)
    G[b].append(a)
    G[a].sort()
    G[b].sort()

# print(G)

# visited, pre, post 리스트 정의와 초기화
#visited = [[] for _ in range(n)]
visited = [False for _ in range(n)]
parent = [None for _ in range(n)]
prev = [0 for _ in range(n)]
post = [0 for _ in range(n)]

# print(visited)
# print(parent)
# print(prev)
# print(post)

# curr_time = 1로 초기화
curr_time = 1

DFSAll(G)

# 출력
# print(visited)
# print(parent)
# print(prev)
# print(post)

order = sorted(prev)  # 크기 작은 순서대로 새로운 리스트 만듦 -> * 오름차순한 원소들을 인덱스로 사용 *
# print(order)
for i in order:
    print(prev.index(i), end=" ")  # prev의 원소 크기 작은 순서대로 출력

print()

for i in range(0, n):
    print([prev[i], post[i]], end=" ")
