class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def get_token_list(expr):
    # expr은 문자열로 수식을 나타냄
    # expr을 연산자와 피연산자로 나눈 후 리스트에 담아 리턴(연산자와 피연산자 모두 문자열 형식)
    # 연산자는 +,-,*,/,^ 5가지 이항연산자만 다루고, 연산자와 피연산자 사이에 "공백이 올 수도 있고 공백이 없을 수도 있음"
    # 모든 피연산자는 float으로 변환
    # 한 자리 이상의 실수가 등장할 수 있다 ex) 10.5
    # 두 가지 경우 처리 1) 3+ 2* 4/(6- 1) <----> 2) 3.14 * 10 <----> 3)3+ 2* 4/(6- 1) + (7 - 1)
    token_list = []
    tmp = ""
    for i in list(expr):
        if i in '+-*/^':
            if tmp == '':
                token_list.append(i)
            else:
                token_list.append(float(tmp)) 
                token_list.append(i)
                tmp = ""
        elif i == '(':
            token_list.append(i)
        elif i == ')':                  # 마지막이 )) 인경우 런타임에러
            if tmp == '':
                token_list.append(i)
            else:
                token_list.append(float(tmp)) 
                token_list.append(i)
                tmp = ""
        elif i == " ":
            pass
        else:
            tmp += i
    if tmp == '':
        return token_list
    else:
        token_list.append(float(tmp)) #맨마지막이 괄호로 끝나지 않는 경우에는 얘를 추가해야되는데.....*** 여기가 문제***
        return token_list

def infix_to_postfix(token_list):
    # token_list는 수식의 연산자가 피연산자가 infix 수식의 순서대로 저장된 리스트
    # 예) token_list = ['3.14', '+', '12']
    # token_list를 postfix 수식으로 변환하고 그 결과를 리스트에 담아 리턴
    opstack = Stack()
    outstack = []
    #token_list = infix.split()

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0 # 우선순위 가장 낮다
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:        # 여기에 오류 하나 있는듯! **
        if type(token) == float:
            outstack.append(token) # outstack은 리스트이므로 append
        else:
            if token == '(':
                opstack.push(token)
            elif token == ')':
                while opstack.top() != '(':
                    outstack.append(opstack.pop())
                opstack.pop() # '('까지 pop -> 얘는 outstack에 저장할 필요 x
            elif token in '+-/*^': # 우선순위가 높거나 같은 연산자 pop
                if opstack.__len__() == 0:
                    opstack.push(token)
                else:
                    if prec.get(token) <= prec.get(opstack.top()):
                        outstack.append(opstack.pop())
                        opstack.push(token)
                    else:
                        opstack.push(token)
        

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while opstack.__len__() != 0:
      outstack.append(opstack.pop())
    return outstack

def compute_postfix(token_list):  
    # postfix 형식의 token_list에 대한 계산 값을 리턴
    # 예) toekn_list = ['3.14', '12', '+']
    S = Stack()
    for token in token_list:
        if type(token) == float:
            S.push(token) 
        else:
            b = S.pop()
            a = S.pop()
            if token == '+':
                S.push(a+b)
            elif token == '-':
                S.push(a-b)
            elif token == '*':
                S.push(a*b)
            elif token == '/':
                S.push(a/b)
            else:
                S.push(a^b)           
    return S.pop()   # "%f" % S.pop()

expr = input() # 문자열 입력 받음
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
#print(infix_to_postfix([3.0, '+', 2.0, '*', 4.0, '/', '(', 6.0, '-', 1.0, ')']))
#print(compute_postfix(infix_to_postfix(get_token_list(expr))))