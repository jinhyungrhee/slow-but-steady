import random


class Heap:  # min_heap
    def __init__(self, L=[]):
        self.A = L

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):  # 인접한 세 노드 사이의 비교
        while n > 2*k + 1:  # 자식 노드가 있는가?
            L, R = 2*k + 1, 2*k + 2
            m = k  # m = (A[k], A[L], A[R]) 중 작은 값을 가지는 index
            if self.A[k] > self.A[L]:
                m = L
            if n > R:  # (??) n = 노드의 개수, R = 2*k+2(오른쪽 자식 인덱스) - 'n < R'과 무슨 차이?
                if self.A[m] > self.A[R]:
                    m = R
            if k == m:  # 내가 가장 작은 값이면
                break
            else:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m

    def make_heap(self):  # 차례대로 모든 애들에 대해서 heapify_down적용 (leaf노드부터 거꾸로)
        n = (len(self.A))
        for k in range(n - 1, -1, -1):  # 마지막 인덱스(n-1)부터 root(0)까지 뒤에서 하나씩
            self.heapify_down(k, n)

    def heap_sort(self):  # heap을 이용한 정렬 (보류)
        n = len(self.A)
        for k in range(len(self.A) - 1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]  # 첫번째와 마지막 교환
            n = n - 1  # A[n-1]은 정렬되었으므로 (작은 수 하나씩 제외시킴)
            self.heapify_down(0, n)

    def heapify_up(self, k):  # 올라가면서 A[k]를 재배치 => OK
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)


S = [random.randint(0, 100) for _ in range(8)]
H = Heap(S)
print("Original: ", H)
H.heap_sort()
H.make_heap()
print("Heapified: ", H)
#insert = 1
# H.insert(insert)
# print("inserted: ", H)  # heapify_up은 제대로 동작함
