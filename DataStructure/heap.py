class Heap:
    def __init__(self, L=[]): # default: 빈 리스트
        self.A = L
        self.make_heap() # A의 값을 힙성질이 만족되도록 make_heap함수 호출

    def __str__(self):
            return str(self.A)

    def heapify_down(self, k, n):
        # n = 힙의 전체 노드수 (heap_sort를 위해 필요함)
        # A[k]를 힙 성질을 만족하는 위치로 내려가면서 재배치
        while 2*k+1 < n: 
            L, R = 2*k + 1, 2*k + 2
            if self.A[L] > self.A[k]:
                m = L
            else :
                m = k
            if R < n and self.A[R] > self.A[m]:
                m = R
            # m = A[k], A[L], A[R] 중 최대값의 인덱스

            if m != k: #A[k]가 최대값이 아니면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break
                

    def make_heap(self):
        n =len(self.A)
        for k in range(n-1, -1, -1): # A[n-1] -> A[0]
            self.heapify_down(k, n)
            
    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n - 1 # A[n-1]은 정렬되었으므로
            self.heapify_down(0, n)

    def heapify_up(self, k): # 올라가면서 A[k]를 재배치
        while k>0 and self.A[(k-1)//2] < self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
            k = (k-1)//2

    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_max(self):
        if len(self.A) == 0 : return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
        self.A.pop() # 실제로 리스트에서 delete!
        self.heapify_down(0, len(self.A)) # len(A) = n-1
        return key


heap = Heap([2, 8, 6, 1, 10, 15, 3, 12, 11])
print(heap)
heap.delete_max()
print(heap)
heap.insert(19)
print(heap)
heap.heap_sort()
print(heap)