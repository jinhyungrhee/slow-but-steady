class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=" ")
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

# find_loc은 search와 insert에 사용하기 위해 선언!
    def find_loc(self, key): # key값 노드가 있으면 해당노드 리턴, 없으면 부모노드 리턴
        if self.size == 0: return None # 빈 리스트면 None 리턴
        p = None # parent of v
        v = self.root
        while v: # root->...->leaf
            if v.key == key: return v
            elif v.key < key:
                p = v
                v = v.right
            else: # v.key > key
                p = v
                v = v.left
        return p # key값이 tree에 없으면 부모노드 리턴(insert연산에 사용!)
                 # p가 None이면 root노드?

    def search(self, key): # find_loc과 다름 없음
        v = self.find_loc(key)
        if v and v.key == key:
            return v
        else:
            return None

    def insert(self, key): # 부모노드(p)를 기준으로 왼쪽 또는 오른쪽에 삽입
        p = self.find_loc(key) # key값을 찾고
        if p == None or p.key != key: # key값이 없으면
            v = Node(key) # 새로운 노드 생성!
            if p == None: # p가 None을 리턴했다면 root 노드!
                self.root = v 
            else: # root노드가 아니면 새로운 노드(v)가 부모노드(p)의 왼쪽에 들어갈 것인지 오른쪽에 들어갈 것인지 결정.
                v.parent = p
                if p.key >= key: # 부모노드(p)의 key값이 새로운 노드의 key값보다 크거나 같으면
                    p.left = v   # 새로운 노드를 왼쪽 자식노드로 삽입
                else: # 부모노드(p)의 key값이 새로운 노드의 key값보다 작으면
                    p.right = v  # 새로운 노드를 오른쪽 자식노드로 삽입
            self.size += 1
            return v # 새로 삽입된 노드를 리턴->다른 연산에 사용
        else: # key값이 이미 있으면 None
            return None

    def deleteByMerging(self, x):
        a = x.left
        b = x.right
        pt = x.parent
        # c = x 자리를 대체할 노드
        # m = 왼쪽 트리(L)에서 가장 큰 노드
        if a != None: # <경우1>: a노드(L트리의 루트노드)가 있느냐 없느냐
            c = a
            m = a # m 찾기
            while m.right: # None이 아닌 동안
                m = right
            if b != None:
                b.parent = m
                m.right = b
        else: # a == None
            c = b
        if pt != None: # <경우2>: 지우려는 x가 root노드냐 아니냐
            if c: # c가 None이 아니여야만 c.parent가 존재***
               c.parent = pt
            if pt.key < c.key:
                pt.right = c
            else:
                pt.left = c
        else: # pt == None (root노드이면)
            self.root = c
            if c: # c가 None이 아니여야만 c.parent가 존재***
                c.parent = None # root노드의 parent는 None 
        self.size += 1
        

    def deleteByCopying(self, x):

T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))