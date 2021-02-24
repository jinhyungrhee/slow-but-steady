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
        if a != None: # <경우1>: a노드(L트리의 루트노드)가 있느냐 없느냐
            c = a # c = x 자리를 대체할 노드 -> L트리가 있으면 a가 x자리 대체 ***
            m = a # m = 왼쪽 트리(L)에서 가장 큰 노드 -> m 찾기
            while m.right: # m.right이 None이 나오면 leaf노드에 도달
                m = m.right
            if b != None: # b노드(R트리의 루트노드)가 있으면 m노드의 자식으로 들어옴
                b.parent = m 
                m.right = b
        else: # a == None (왼쪽 서브트리가 없으면)
            c = b # b노드(오른쪽 서브트리의 루트노드)가 x자리 대체 ***

        # x.parent와 x를 대체할 a 또는 c의 링크 연결!
        # <경우2>: 삭제할 노드 x가 T.root인 경우와 아닌 경우
        if pt != None: 
            if c: # c가 None이 아니여야만 c.parent가 존재***
               c.parent = pt # 새로운 노드의 부모를 x의 parent로 연결
            if pt.key < c.key:
                pt.right = c
            else:
                pt.left = c
        else: # pt == None (root노드이면)
            self.root = c
            if c: # c가 None이 아니여야만 c.parent가 존재***
                c.parent = None # root노드의 parent는 None 
        self.size -= 1

    '''비교
    def deleteByMerging(self, x):
        # assume that x is not None
        a, b, pt = x.left, x.right, x.parent
        if a == None: c = b
        else: # a != None
            c = m = a
            # find the largest leaf m in the subtree of a
            while m.right:
                m = m.right
            m.right = b
            if b: b.parent = m

        # 찾은 c를 가지고 경우의 수 계산
        if self.root == x: # c becomes a new root
            if c: c.parent = None
            self.root = c
        else: # c becomes a child of pt of x
            if pt.left == x: pt.left = c
            else: pt.right = c
            if c: c.parent = pt
        self.size -= 1
    '''
        
    def deleteByCopying(self, x):
        a, b, pt = x.left, x.right, x.parent
        # m = L에서 가장 큰 노드
        if a != None: # L이 존재하면
            m = a # m(L에서 가장 큰 노드)찾기
            while m.right: # m.right이 None이 아닌 동안(m.right이 None이 나오면 leaf노드)
                m = m.right
            x.key = m.key # L에서 가장 큰 노드의 key값 x에 copy
            if m.left != None:  # m의 왼쪽 서브트리가 존재하면,
                m = m.left
                a.right = m.left
                m.left.parent = a
        elif a == None and b != None: # L이 존재하지 않고, R이 존재하는 경우
            # y = R에서 가장 작은 노드
            y = b # y(R에서 가장 작은 노드) 찾기
            while y.left: # y.left가 None이 아닌 동안(y.left가 None이 나오면 leaf노드)
                y = y.left
            x.key = y.key
            if y.right != None: # y의 오른쪽 서브트리가 존재하면,
                y = y.right
                b.left = y.right
                y.right.parent = b
        elif a == None and b == None:
            pt.right = None
            


T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")