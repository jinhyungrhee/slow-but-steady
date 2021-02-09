'''
스택활용예3 : Postfix 계산 => 테스트케이스 7/7
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
            print("Stack is Empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def compute_postfix(postfix):

    S = Stack()
    token_list = postfix.split(' ')

    for token in token_list:
        if token in '+-*/^':
            b = float(S.pop())  # 먼저 나오는 연산자가 뒤
            a = float(S.pop())  # 나중에 나오는 연산자가 앞
            if token == '+':
                S.push(a + b)
            elif token == '-':
                S.push(a - b)
            elif token == '*':
                S.push(a * b)
            elif token == '/':
                S.push(a / b)
            else:
                S.push(a ^ b)
        else: # operand이면
            S.push(token)
    return "%0.4f" % S.pop() # 마지막에 남은게 최종 결과 값 -> 소수점 4자리까지 표현

postfix_expr = input()
result = compute_postfix(postfix_expr)
print(result)