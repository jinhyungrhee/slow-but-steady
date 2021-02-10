'''
Dequeue예제 : Palindrome check => class Dequeue 직접 구현해보기!
'''

# from collections import deque

class deque:
    def __init__(self, s):
        self.items = list(s) # 문자열을 한글자씩 끊어 리스트로 만들기

    def append(self, c):
        self.items.append(c)
    
    def appendleft(self, c):
        self.items.insert(0, c) # insert에 인덱스 번호 입력하면 그곳에 삽입

    def pop(self):
        try:
            return self.items.pop() # 리스트의 맨 마지막 값 pop
        except IndexError:
            print("deque is empty")

    def popleft(self):
        try:
            return self.items.pop(0) # 리스트의 맨 처음 값 pop
        except:
            print("deque is empty")

    def __len__(self):
        return len(self.items)

    def right(self):
        return self.items[-1] # 리스트의 가장 마지막 값 리턴

    def left(self):
        return self.items[0] # 리스트의 가장 처음 값 리턴

def check_palindrome(s):
    dq = deque(s)
    palindrome = True # 초기값 True로 설정
    while len(dq) > 1: # dq에 남은게 하나가 될 때 까지
        if dq.popleft() != dq.pop(): # 양쪽 가장자리에 있는 것 하나씩 빼면서 비교
            palindrome = False
    return palindrome

i = input()
result = check_palindrome(i)
print(result)