class Heap:
    def __init__(self, L=[]):
        self.A = L
    def __str__(self):
        return str(self.A)
    def __len__(self):
        return len(self.A)

    def heapify_down(self, k, n): # A[k]를 자식노드의 값과 비교하면서 더 큰 값을 갖는 자식노드와 swap
        # n = 힙의 전체 노드수(heap_sort를 위해 필요)
        # A[k]가 힙 성질을 위배한다면, 밑으로 내려가면서 힙 성질을 만족하는 위치를 찾음!
        while 2*k+1 < n:
            L, R = 2*k + 1, 2*k + 2 # A[k]의 왼쪽 자식노드=A[2*k+1], 오른쪽 자식노드=A[2*k+2] (부모노드=A[(k-1)/2])
            if L < n and self.A[L] > self.A[k]: # 왼쪽 자식노드 값이 부모노드의 값 보다 크면
                m = L                           # 왼쪽 자식노드 값이 최대(m)
            else:
                m = k
            if R < n and self.A[R] > self.A[m]: # 오른쪽 자식노드 값이 부모노드의 값 보다 크면
                m = R                           # 오른쪽 자식노드 값이 최대(m)
            if m != k:  # A[k]가 최대값이 아니면 힙 성질 위배 -> m과 k를 swap
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1): # A[n-1] -> ... -> A[0]
            self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n - 1 # A[n-1]은 정렬되었으므로
            self.heapify_down(0, n)

S = [int(x) for x in input().split()]
H = Heap(S)
H.make_heap()
H.heap_sort()
print(H)