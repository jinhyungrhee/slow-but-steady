class AdaptedHeap:  # min_heap
    def __init__(self):
        self.A = []
        self.D = {}  # dict D[key] = index

    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    def insert(self, key):
        self.A.append(key)
        k = self.heapify_up(len(self.A) - 1)  # 맨 뒤에서부터 heapify_up
        #self.D[key] = k
        return k  # key값이 최종 저장된 index리턴

    # 올라가면서 A[k]를 재배치 ("k는 인덱스") - key값의 인덱스가 변경되면 그에따라 D변경 필요 ***
    def heapify_up(self, k):
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            # 변경된 index 딕셔너리에 반영
            # heapify_up한 경우 딕셔너리 인덱스 update (1)
            self.D[self.A[k]], self.D[self.A[(k - 1) // 2]] = ((k - 1) // 2), k
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            k = (k - 1) // 2  # 부모의 인덱스와 바꿈
        self.D[self.A[k]] = k  # heapfiy_up 안 한 경우 딕셔너리 인덱스 update (2)
        return k  # heapfiy_up 하면 0리턴 heapify_up 안하면 k리턴

    def heapify_down(self, k):  # 인접한 세 노드 사이의 비교 - n은 노드의 개수 (D변경해야함!)
        while len(self.A) > 2*k + 1:  # 자식 노드가 있는가?
            L, R = 2*k + 1, 2*k + 2
            m = k  # m = (A[k], A[L], A[R]) 중 작은 값을 가지는 index
            if self.A[k] > self.A[L]:
                m = L
            if len(self.A) > R:  # (??) n = 노드의 개수, R = 2*k+2(오른쪽 자식 인덱스) - 'n < R'과 무슨 차이?
                if self.A[m] > self.A[R]:
                    m = R
            if k == m:  # 내가 가장 작은 값이면
                break
            else:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                self.D[self.A[k]], self.D[self.A[m]
                                          ] = self.D[self.A[m]], self.D[self.A[k]]
                k = m
        return k

    def find_min(self):
        if len(self.A) == 0:
            return None
        else:
            return self.A[0]

    def delete_min(self):
        if len(self.A) == 0:
            return None
        else:
            x = self.A.pop(0)
            del self.D[x]
            for i in self.D:
                self.D[i] -= 1
            for i in range(0, len(self.A)):
                self.heapify_down(self.D[self.A[i]])  # ?
            return x

    # new_key값이 "최종 저장된 index" 리턴(update(13, 1)하면 0 리턴)
    def update_key(self, old_key, new_key):
        '''
        for i in range(0, len(self.A)):
            if self.A[i] == old_key:
                self.A[i] = new_key
                self.D[]
                return i
        return None
        '''
        try:
            if self.D[old_key] or self.D[old_key] == 0:
                self.A[self.D[old_key]] = new_key
                self.D[new_key] = self.D.pop(old_key)  # dict update!
                if old_key > new_key:
                    x = self.heapify_up(self.D[new_key])
                else:
                    x = self.heapify_down(self.D[new_key])
                return x
        except:
            return None


'''
    def make_heap(self):
        n = len(self.A)
        for k in range(0, n):
'''


H = AdaptedHeap()

# print(H.insert(2))  # dict [2] 반영x - 밀려난 애들도 반영해야함 -> 아마도 update()?
# print(H.insert(5))  # dict [3] 반영x
print(H.insert(3))
print(H.insert(5))
print(H.insert(13))
print(H.insert(8))
print(H.insert(9))
print(H.update_key(13, 1))
print(H.update_key(1, 17))

print(H)
# print(H.find_min())
print(H.delete_min())
print(H)
print(H.D)
#print(H.update_key(13, 1))
print(H)
# print(H.update_key(1, 17))  # 이때는 heapify_down으로 내려와야함...
print(H)
print(H.D)
'''

H = AdaptedHeap()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        key = int(cmd[1])
        loc = H.insert(key)
        print(f"+ {int(cmd[1])} is inserted")
    elif cmd[0] == 'find_min':
        m_key = H.find_min()
        if m_key != None:
            print(f"* {m_key} is the minimum")
        else:
            print(f"* heap is empty")
    elif cmd[0] == 'delete_min':
        m_key = H.delete_min()
        if m_key != None:
            print(f"* {m_key} is the minimum, then deleted")
        else:
            print(f"* heap is empty")
    elif cmd[0] == 'update':
        old_key, new_key = int(cmd[1]), int(cmd[2])
        idx = H.update_key(old_key, new_key)
        if idx == None:
            print(f"* {old_key} is not in heap")
        else:
            print(f"~ {old_key} is updated to {new_key}")
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
'''
