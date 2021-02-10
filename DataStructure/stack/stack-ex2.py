'''
스택활용예2 : Infix to Postfix => 테스트케이스 6/7 (**다시 생각해보기**) 
'''

class Stack:
    def __init__(self):
        self.items = [] # 리스트 초기화

    def push(self, val):
        self.items.append(val) # 리스트에 값 추가

    def pop(self):
        try:
            return self.items.pop() # 리스트에 값이 있으면 pop
        except IndexError:
            print("Stack is empty") # 값이 없으면 error 메시지

    def top(self):
        try:
            return self.items[-1] # 리스트 맨 뒤 값(= stack에서는 맨 위 값) 리턴
        except IndexError:
            print("Stack is empty") # 값이 없으면 error 메시지
    
    def __len__(self):  # 리스트(stack)의 items수 리턴
        return len(self.items)

    def isEmpty(self):  # 리스트의 items수가 0이면 True 리턴
        return self.__len__() == 0


def infix_to_postfix(infix):

    opstack = Stack()   # 괄호와 연산자 저장(Stack)
    outstack = []       # 피연산자와 Postfix 수식 결과를 저장(리스트)
    token_list = infix.split(' ') # infix수식을 tokenize해서 연산자와 operand들의 리스트 token_list를 얻는다.

    #연산자 우선순위 설정 (*딕셔너리*)
    prec = {}
    prec['('] = 0   # '('는 가장 마지막에(또는 ')'를 만났을 때만) 나와야 하므로 우선순위 가장 낮다
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 2

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop() # 아직 남아있는 '(' 제거
        elif token in '+-/*^': # 우선순위가 높거나 같은 연산자가 opstack안에 있으면 pop시키고 outstack에 추가
            if opstack.__len__() == 0: # opstack이 빈 경우에는 그냥 들어감.
                opstack.push(token)
            else:
                if prec.get(token) <= prec.get(opstack.top()): # *주의 : opstack.top()이 None이어서 비교연산자 error 생겼음*
                    outstack.append(opstack.pop())
                    opstack.push(token)
                else:
                    opstack.push(token)
        else: # operand(피연산자)일 때
            outstack.append(token)

    # 마지막으로 opstack에 남은 모든 연산자를 pop 후 outstack에 append
    while opstack.__len__() != 0:
        outstack.append(opstack.pop())

    return " ".join(outstack)

infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)