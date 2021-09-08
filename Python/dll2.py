class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # create an empty list with only dummy node

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v.key) for v in self)

    def printList(self):
        v = self.head.next
        print("h -> ", end="")
        while v != self.head:
            print(str(v.key)+" -> ", end="")
            v = v.next
        print("h")

    #        def isEmpty(self):
    #            return self.head.next == self.head

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        # cut [a..b]
        a.prev.next = b.next
        b.next.prev = a.prev
        # insert [a..b] after x
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a
        
    def moveAfter(self, a, x):
        self.splice(a, a, x)
        
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
        
    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)
        #self.size += 1
        
    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
        #self.size += 1
        
    def pushFront(self, key):
        self.insertAfter(self.head, key)
        
    def pushBack(self, key):
        self.insertBefore(self.head, key)
        
    def deleteNode(self, x): # key값으로 들어오는게 아니라 노드로 들어온다... // node로 들어오는 경우와 값으로 들어오는 경우 둘다 처리?
        if self.search(x) == None: # x가 노드인 경우
            if x == None or x == self.head:
                return
            m = x.key
            x.prev.next = x.next
            x.next.prev = x.prev
            del x
            return m
        else: # x가 값(key)인 경우
            n = self.search(x)
            if n == None or n == self.head:
                return
            n.prev.next = n.next
            n.next.prev = n.prev
            del n
            return x

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(key)
        return key

    def popBack(self):
        if self.head.next == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(key)
        return key
        
    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        if v.key == key:
            return v
        return None

    def first(self):
        if self.head.next == self.head:
            return None
        return self.head.next.key

    def last(self):
        if self.head.next == self.head:
            return None
        return self.head.prev.key

    def findMax(self):
        if self.head.next == self.head:
            return None
        else:
            v = self.head.next
            m = self.head.next.key
            while v.next != self.head:
                if v.key <= v.next.key:
                    if m <= v.next.key:
                        m = v.next.key
                    else:
                        pass
                else:
                    if m < v.key:
                        m = v.key
                    else:
                        pass
                v = v.next
            if v.key > m:
                m = v.key
            return m
		
    def deleteMax(self): # findMax deleteNode, deleteMax 문제 없음
        if self.head.next == self.head:
            return None
        else:
            x = self.findMax()
            return self.deleteNode(x)
		
    def sort(self): # 마지막 원소 하나 누락되는 문제... 왜지?
        #v = self.head.next
        tmp = []
        while self.head.next.key != None:
            tmp.append(self.deleteMax())
            #v = v.next
        #tmp.append(self.deleteMax())
        print(tmp)
        for i in tmp:
            self.pushFront(i)
        return self

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
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
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
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")
'''
L.pushFront(30)
L.pushBack(10)
L.pushBack(20)
L.pushBack(50)
L.pushFront(1)
L.pushFront(2)
L.pushFront(7)
L.insertAfter(L.search(50), 3)
L.insertBefore(L.search(20), 5)
L.printList()
L.sort()    # 원소가 6개부터 sort가 이상해지기 시작함 + sort가 진행되고 난 결과에 대해서 어떠한 연산을 할 수 없음!

print(L.search(2))
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())
print(L.deleteMax())


L.printList()
'''