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
	
	def printList(self): # 변경없이 사용할 것!
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
		if len(self) == 0:
			self.head = v
		else:
			tail = self.head # tail찾기(running technique)
			while tail.next != None:
				tail = tail.next
			tail.next = v
		self.size += 1
		
	def popFront(self): # head 노드의 값 리턴. empty list이면 None 리턴
		if len(self) == 0:
			return None
		else:
			x = self.head
			key = x.key
			self.head = x.next
			self.size -= 1
			del x
			return key
		
	def popBack(self): # tail 노드의 값 리턴. empty list이면 None 리턴
		if len(self) == 0:
			return None
		else: 
			prev = None
			tail = self.head
			while tail.next != None: #running technique - tail과 바로 전 노드 찾기
				prev = tail
				tail = tail.next
			if len(self) == 1: # 노드가 하나면 prev가 head가 되고 tail은 None
				self.head = None
			else:
				prev.next = tail.next # 노드가 두개 이상이면 tail 전노드와 tail 다음노드 연결
			key = tail.key
			del tail
			self.size -= 1
			return key
		
	def search(self, key): # key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head
		while v != None:
			if v.key == key:
				return v
			v = v.next
		return v
	
	def remove(self, x): # 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴! x는 key 값이 아니라 노드임에 유의!
		if x == None or self.head == None: return None
		key = x.key
		if x == self.head:
			return self.popFront()
		else:
			prev, tail = None, self.head
			while tail != None and tail != x:
				prev = tail
				tail = tail.next
			if tail == x:
				prev.next = tail.next
			del x
			self.size -= 1
			return key
		
	def reverse(self, key):
		v = self.search(key) # 찾은 노드
		prev, curr = None, self.head
		while curr != None and curr != v:
			prev = curr
			curr = curr.next
		if v == None:
			return # 아무 일도 하지 않음 (or pass?)
		else:
			a, b = None, v
			while b: 
				if b:
					c = b.next
					b.next = a # 맨 첫 노드 뒤에 None이 붙고 이것은 끝까지 감!
				a = b
				b = c
			if prev == None:
				self.head = a
			else:
				prev.next = a # a에 역순으로 연결되어있고 a를 head로 만드는것! # a = 5 -> 4 -> 3
	
	def findMax(self):
		# self가 empty이면 None, 아니면 max key 리턴
		if self.size == 0:
			return None
		elif self.size == 1:
			return self.head.key
		else:
			v = self.head
			m = self.head.key
			while v.next != None:
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
			return m

	def deleteMax(self):
		# self가 empty이면 None, 아니면 max key 지운 후, max key 리턴
		if self.size == 0:
			return None
		else:
			x = self.search(self.findMax())  # x는 key 값임 -> search로 노드 찾아서 리턴
			return self.remove(x) # x는 노드임


	def insert(self, k, val):
		if self.size <= k:
			self.pushBack(val)
		else:
			n = Node(val) # 새로운 노드 생성
			prev, v = None, self.head
			for i in range(0, k):
				prev = v
				v = v.next
				i += 1
			prev.next = n
			n.next = v

	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
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
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
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
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")