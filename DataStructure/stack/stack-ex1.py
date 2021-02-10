'''
스택활용예1 : 괄호 맞추기
'''

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is emtpry")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is emtpry")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

parSeq = input()

def parChecker(parSeq):
    S = Stack()
    for symbol in parSeq:
        if symbol in parSeq:
            if symbol == "(":
                S.push(symbol)
            else:
                if S.isEmpty():
                    return False
                else:
                    S.pop()
    if S.isEmpty():
        return True
    else:
        return False

'''
def parChecker(parSeq):
    S = Stack()
    for p in parSeq:
        if p == "(":
            S.push(p)
        elif p == ")":
            S.pop()
        else:
            print("Not Allowed Symbol")    => something went worng
    if S.isEmpty():
        return True
    else:
        return False
'''

print(parChecker(parSeq)) 