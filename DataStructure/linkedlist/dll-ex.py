'''
마지막 pushBack 추가 안 되는 문제
'''

class Node:
    def __init__(self, key=None): # dummy node는 자기 자신을 가리킴
        self.key = key
        self.next = self
        self.prev = self

    def __str(self): # print(node)인 경우 출력할 문자열
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    '''
    def __len__(self):
        return self.size
    '''
    def isEmtpy(self):
        return self.size == 0 # 0이면 true 아니면 false 리턴

    def splice(self, a, b, x): # [a..b]까지의 노드를 잘라서 x노드 뒤에 붙여넣기
        if a == None or b == None or x == None:
            return
        ap = a.prev # ap is previous node of a
        bn = b.next # bn is next node of b

        # cut[a..b]
        ap.next = bn # a 앞노드를 b 뒷노드와 연결
        bn.prev = ap # b 뒷노드를 a 앞노드와 연결

        #insert[a..b] after x
        xn = x.next
        xn.prev = b # x 다음 노드의 앞부분을 b와 연결
        b.next = xn # (양방향으로 연결)
        a.prev = x  # a의 앞부분을 x와 연결
        x.next = a  # (양방향으로 연결)

    def moveAfter(self, a, x):
        self.splice(a, a, x) # [a..a] = a를 잘라내서 x 뒤에 붙여넣기
    
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev) # a를 잘라내서 x 앞에 붙여넣기

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x) # 새로운 key의 노드를 생성해서 x 뒤에 붙여넣기
    
    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def deleteNode(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
    
    def popFront(self):
        if self.size == 0:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        return key

    def popBack(self):
        if self.size == 0:
            return None
        key = self.head.prev.key # dummy node 전 노드가 가장 마지막 노드
        self.deleteNode(self.head.prev)
        return key

    def search(self, key):
        v = self.head # dummy node
        while v.next != self.head: # running technique
            if v.key == key:
                return v
            v = v.next
        return None # or return v(동일)

    def first(self):
        if self.size == 0:
            return None
        return self.head.next.key

    def last(self):
        if self.size == 0:
            return None
        return self.head.prev.key

    def printList(self):
        v = self.head
        while v.next != self.head:
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA': # inserta key_x key: key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB': # insertb key_x key : key의 새 노드를 key_X를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == 'first':
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == 'last':
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit': # while문을 돌면서 계속 input을 받다가 'exit'을 치면 break로 while문 빠져나옴
        break
    else:
        print("* not allowed command. enter a proper command!")

