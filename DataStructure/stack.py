class Stack:
    def __init__(self):
        self.items = []     # 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try :                       # pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:          # indexError 발생   
            print("Stack is empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
        
    def __len__(self):          # len()로 호출하면 stack의 item수 반환
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0

S = Stack()
S.push(10)
S.push(2)
print(S.top())
print(len(S))
print(S.pop())
print(len(S))
print(S.isEmpty())
print(S.top())