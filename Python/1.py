'''
get_token_list(expr) 여기만 고치면 어느정도는 될듯!!!!
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
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def infix_to_postfix(infix):
    
    opstack = Stack()
    outstack = []
    token_list = infix.split()

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0 # 우선순위 가장 낮다
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3
    prec[None] = 0

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
              outstack.append(opstack.pop())
            opstack.pop()
        elif token in '+-/*^': # 우선순위가 높거나 같은 연산자 pop // opstack : - * +
            if opstack.__len__() == 0:
              opstack.push(token)
            else: # 오류발생 while문 사용 : 3 - 5 * 8 + 7 가 3 5 8 * - 7 + 나와야 하는데 3 5 8 * 7 + - 나옴 (오답) 
                while prec.get(token) <= prec.get(opstack.top()): # opstack.top()이 None이 되면 typeError발생
                    outstack.append(opstack.pop()) 
                opstack.push(token)
        else: # operand일 때
            outstack.append(token) # outstack은 리스트이므로 append

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    while opstack.__len__() != 0:
      outstack.append(opstack.pop())

    return " ".join(outstack)
'''

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
        elif i == ')':
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

'''

print(infix_to_postfix(input()))