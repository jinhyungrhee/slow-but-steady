'''
Singly Linked List 연산 구현 실습 -> 2/5, remove()부분 다시 보기
'''

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def printList(self):
        v = self.head
        while(v):
            print(v.key, "->", end=" ")
            v = v.next
        print("None")

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        self.size += 1   
    
    def pushBack(self, key):
        v = Node(key)
        if len(self) == 0:  # 빈 리스트면 head노드로 v 삽입
            self.head = v
        else:               # 빈 리스트가 아니면
            tail = self.head # running technique: head에서 시작해서 while루프 돌며 head 찾기
            while tail.next != None:
                tail = tail.next
            tail.next = v # None인 곳에다가 v노드 삽입 => 맨 마지막 노드로 추가됨
        self.size += 1

    def popFront(self): # head 노드의 값 리턴. empty list이면 None 리턴
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key # 리턴할 head 노드의 key값
            self.head = x.next
            self.size -= 1
            del x
            return key

    def popBack(self): # tail 노드 값 리턴. empty list이면 None 리턴
        if len(self) == 0: # <<경우 1: 노드가 없으면>>
            return None # None 리턴
        else: # (running technique)
            prev, tail = None, self.head # 'tail노드'와 '바로 전 노드' 찾기
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1: # <<경우 2: 노드가 하나 밖에 없으면>> (prev == None 동일)
                self.head = None # head 노드를 지워야 하므로 linkedlist head에 None 연결
            else: # <<경우3: 노드가 2개 이상이면>>
                prev.next = tail.next # tail 전 노드와 tail 다음 노드 서로 연결
            key = tail.key  # key값 리턴하기 위해 지우기 전에 key값 저장
            del tail
            self.size -= 1
            return key # or return (key, value)

    def search(self, key): # key 값이 저장된 노드 리턴. 없으면 None 리턴
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return v # or return None (v가 None이 되어야 while문 빠져나오기 때문에 결국 같은 의미)

    def remove(self, x): # 노드 x를 제거한 후 True리턴. 제거 실패면 False리턴.
        if len(self) == 0: # <<경우 1: 빈 리스트면 제거 실패 -> False 리턴>>
            return False
        elif self.head.key == x.key: # <<경우 2: 노드가 하나 밖에 없으면 popFront호출>>
            self.popFront()
            return True
        else: # <<경우 3: 노드가 2개 이상인 경우>>
            prev, tail = None, self.head
            while tail.key != x.key: # tail노드 key와 찾는 노드의 key가 같을 때까지 탐색
                prev = tail
                tail = tail.next
            prev.next = tail.next # tail노드와 찾는 노드가 같으면 while 문을 빠져나와 앞-뒤 노드 연결
            del x
            self.size -= 1
            return True
    '''
    def size(self):
        return self.size
    '''

L = SinglyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == "pushFront":
        L.pushFront(int(cmd[1]))
        print(int(cmd[1]), "is pushed at front.")
    elif cmd[0] == "pushBack":
        L.pushBack(int(cmd[1]))
        print(int(cmd[1]), "is pushed at back.")
    elif cmd[0] == "popFront":
        x = L.popFront()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from front.")
    elif cmd[0] == "popBack":
        x = L.popBack()
        if x == None:
            print("List is empty.")
        else:
            print(x, "is popped from back. ")
    elif cmd[0] == "search":
        x = L.search(int(cmd[1]))
        if x == None:
            print(int(cmd[1]), "is not found!")
        else:
            print(int(cmd[1]), "is found!")
    elif cmd[0] == "remove":
        x = L.search(int(cmd[1]))
        if L.remove(x): # true면
            print(x.key, "is removed.")
        else:
            print("key is not removed for some reason.")
    elif cmd[0] == "printList":
        L.printList()
    elif cmd[0] == "size":
        print("list has", len(L), "nodes.")
    elif cmd[0] == "exit":
        print("DONE!")
        break
    else:
        print("Not allowed operation! Enter a legal one!")



