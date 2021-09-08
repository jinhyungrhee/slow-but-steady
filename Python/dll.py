class Node:
	def __init__(self, key="h"):	# 처음 생성된 dummy node는 자기 자신을 가리킴
		self.key = key
		self.next = self
		self.prev = self
		
	def __str__(self):	# print(node)인 경우 출력할 문자열
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # key = "h" 앞 뒤 모두 자기를 가리킴. (dummy node)/pushF는 dummy node 바로 뒤에 연결
		self.size = 0
		
	def __len__(self):
		return self.size
	
	def isEmpty(self):
		return self.__len__() == 0	# 0이면 true 아니면 false 
		
	def splice(self, a, b, x): # cut [a..b] after x
		if a == None or b == None or x == None: # 조건 만족 안하면 아무것도 실행x
			return 
		# cut [a..b]
		a.prev.next = b.next
		b.next.prev = a.prev
		
		# insert [a..b] after x *** 보완필요 *** x = self.head.prev
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
		self.size += 1
		
	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)
		self.size += 1
		
	def pushFront(self, key):
		self.insertAfter(self.head, key)
	
	def pushBack(self, key):
		self.insertBefore(self.head, key)
	
	def deleteNode(self, key): # x를 key값으로 찾지만 아래에서 연산을 수행하는 x는 노드임! 
		x = self.search(key)
		if x == None or x == self.head: # x노드가 존재하지 않거나 dummy node이면 none 리턴
			return
		x.prev.next = x.next
		x.next.prev = x.prev
		del x
		self.size -= 1
		return key
		
	def popFront(self):
		if self.head.next == self.head: # 빈 리스트이면 None 리턴
			return None
		key = self.head.next.key
		self.deleteNode(key)
		return key
	
	def popBack(self):
		if self.head.next == self.head: # 빈 리스트이면 None 리턴
			return None
		key = self.head.prev.key # dummy node 전 노드가 가장 마지막 노드
		self.deleteNode(key)
		return key
	
	def search(self, key):
		v = self.head # dummy node
		while v.next != self.head: # running technique
			if v.key == key:
				return v
			v = v.next
		if v.key == key: # pushBack으로 들어간 맨 마지막 값까지 확인!
			return v
		return None # or return v
	
	def first(self):
		if self.size == 0:
			return None
		return self.head.next.key
	
	def last(self):
		if self.size == 0:
			return None
		return self.head.prev.key
	
	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+"->", end=" ")
			v = v.next
		print("h")

	def findMax(self):
		if self.head.next == self.head: # 빈 리스트면
			return None
		elif self.__len__() == 1:
			return self.head.next.key
		else:
			v = self.head.next
			m = self.head.next.key # v.key
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
				v  = v.next
			if v.key > m:
				m = v.key
			return m
	
	def deleteMax(self):
		if self.size == 0:
			return None
		else:
			x = self.findMax() # x는 key 값임 -> search로 노드 찾아서 리턴
			return self.deleteNode(x) # x는 값임

	def sort(self): # deleteMax와 pushFront 사용 # sort시 None 등장?
		v = self.head.next
		tmp = []
		while v != self.head:
			tmp.append(self.deleteMax())
			v = v.next
		tmp.append(self.deleteMax())
		for i in tmp:
			self.pushFront(Node(i))
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