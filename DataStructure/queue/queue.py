class Queue:
    def __init__(self):
        self.items = []         # 데이터 저장을 위한 리스트 준비
        self.front_index = 0    # 다음 dequeue될 값의 인덱스 기억

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty")
            return None         # dequeue할 아이템이 없음을 의미
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

    def __len__(self):         
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0


# Josephufs game

    def Josephus(self, n, k):
        Q = Queue()
        for v in range(1, n+1):
            Q.enqueue(v)
        while len(Q) > 1:
            for i in range(1, k):
                Q.enqueue(Q.dequeue())
            Q.dequeue()         # k-th number is deleted
        
        return Q.dequeue()      # len(Q) == 1

Q = Queue()
Q.enqueue(5)
Q.enqueue(10)
Q.enqueue(-1)
print(len(Q))
Q.dequeue()
print(len(Q))
