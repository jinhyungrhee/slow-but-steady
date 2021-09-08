class AdaptedHeap:  # min_heap으로 정의함!
    def __init__(self):
        self.A = []
        self.D = {}  # dictionary D[key] = index

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def insert(self, key):
        # code here
        # key 값이 최종 저장된 index를 리턴한다!
        self.A.append(key)
        k = self.heapify_up(len(self.A) - 1)
        return k

    def heapify_up(self, k):
        # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            self.D[self.A[k]], self.D[self.A[(k - 1) // 2]] = (k - 1) // 2, k
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2
        self.D[self.A[k]] = k
        return k

    def heapify_down(self, k):
        # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
        while len(self.A) > 2*k + 1:
            L, R = 2*k + 1, 2*k + 2
            m = k
            if self.A[k] > self.A[L]:
                m = L
            if len(self.A) > R:
                if self.A[m] > self.A[R]:
                    m = R
            if k == m:
                break
            else:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                self.D[self.A[k]], self.D[self.A[m]
                                          ] = self.D[self.A[m]], self.D[self.A[k]]
                k = m
        return k

    def find_min(self):  # error발생
        # 빈 heap이면 None 리턴, 아니면 min 값 리턴
        # code here
        if len(self.A) == 0:
            return None
        else:
            return self.A[0]

    def delete_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
        # code here
        if len(self.A) == 0:
            return None
        else:
            m_key = self.A[0]
            self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
            self.D[self.A[0]], self.D[self.A[len(
                self.A)-1]] = self.D[self.A[len(self.A)-1]], self.D[self.A[0]]
            x = self.A.pop()
            del self.D[x]
            for i in range(0, len(self.A)):
                self.heapify_down(self.D[self.A[i]])
            return m_key

    def update_key(self, old_key, new_key):
        # old_key가 힙에 없으면 None 리턴
        # 아니면, new_key 값이 최종 저장된 index 리턴
        # code here
        try:
            if self.D[old_key] or self.D[old_key] == 0:  # 이 딕셔너리는 힙의 인덱스표시
                self.A[self.D[old_key]] = new_key
                self.D[new_key] = self.D.pop(old_key)  # dict update
                if old_key > new_key:
                    for i in range(0, len(self.A)):
                        # self.heapify_up(self.D[self.A[i]])  # 여기를 고쳐야할듯!
                        self.heapify_up(self.A[i])  # 여기를 고쳐야할듯!
                else:
                    for i in range(0, len(self.A)):
                        self.heapify_down(self.D[self.A[i]])
                return self.D[new_key]
        except:
            return None


def dijkstra(G):
    s = 0  # node 0 is source
    dist = [float('inf') for _ in range(n)]  # 노드 개수만큼 필요
    dist[0] = 0  # s의 초기 dist값은 0 -> [0, inf, inf, inf ... inf]
    parent = [None for _ in range(n)]  # parent 사용 **
    parent[0] = 0
    Q = AdaptedHeap()  # dist[]리스트와 adaptedHeap Q와의 관계 *** (잘 생각해보기)
    for i in dist:  # heap에 dist값을 key값으로 집어 넣음(인덱스가 노드번호)
        Q.insert((i))
#   while len(Q) != 0:
        #    print(Q)
        #    print(Q.D)
    u = Q.delete_min()  # dist값이 최소인 노드(u) 힙에서 삭제 // u = 0
    #Q.D[float('inf')] += 1
#    print(Q)
#    print(Q.D)
    # u의 인접노드(v)에 대해서 relax // [1,5], [2,8],[3,1],[4,3]
    tmp = dist.index(u)
    for i in range(len(G[tmp])):
        # relax (더 짧은 거리로 dist값 업데이트) -> 이거를 힙에서 업데이트 해야하나?? ****
        #    print(i)
        # [0, inf, inf, inf, inf ... inf] => heap의 key값은 "현재 그 노드의 dist값"임!
        #        break
        # for i in range(len(G[u])):
        # G[u][i][0] => 1 2 3 4 (인접노드들) // u = 0 // G[u][i][1] = w
        #old_val = dist[G[u][i][0]]
        if dist[G[tmp][i][0]] > dist[tmp] + G[tmp][i][1]:  # relax
            #Q.update_key(dist[G[tmp][i][0]], dist[tmp] + G[tmp][i][1])
            dist[G[tmp][i][0]] = dist[tmp] + G[tmp][i][1]
            parent[G[tmp][i][0]] = tmp


n = 10
m = 14
G = [[[1, 5], [2, 8], [3, 1], [4, 3]], [[2, 8]], [[4, 5]], [[4, 8], [
    9, 6], [2, 8]], [[0, 4], [2, 1]], [], [[3, 7]], [], [[0, 1]], [[3, 3]]]
