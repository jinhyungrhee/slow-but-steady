'''
* 윤다영 학생 코드
'''


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:  # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
        self.fixHeight(v)
        self.size += 1
        return v

    def fixHeight(self, x):  # x의 왼쪽 오른쪽을 비교해 x부터 root 까지 heigth 부여
        while x:
            # x의 자식이 없는 경우 ( x는 leaf 노드)
            if x.left == None and x.right == None:
                x.height = 0
            elif x.left != None and x.right == None:  # x의 왼쪽만 있음
                x.height = x.left.height + 1
            elif x.left == None and x.right != None:  # x의 오른쪽만 있음
                x.height = x.right.height + 1
            else:  # 왼 오 다 있을 떄 큰 쪽 따라감
                if x.left.height > x.right.height:
                    x.height = x.left.height + 1
                else:
                    x.height = x.right.height + 1
            x = x.parent
        return

    def deleteByMerging(self, x):
        # assume that x is not None
        a, b, pt = x.left, x.right, x.parent
        m = None
        if a == None:
            c = b
        else:  # a != None
            c = m = a
            # find the largest leaf m in the subtree of a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m

        if self.root == x:  # c becomes a new root
            if c:
                c.parent = None
            self.root = c

        else:  # c becomes a child of pt of x
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1

        if m:
            self.fixHeight(m)
        else:
            self.fixHeight(pt)

    # 노드들의 height 정보 update 필요

    def deleteByCopying(self, x):
        if x == None:
            return None
        pt, L, R = x.parent, x.left, x.right
        if L:  # L이 있음
            y = L
            while y.right:
                y = y.right
            x.key = y.key
            if y.left:
                y.left.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.left
            else:
                y.parent.right = y.left
            self.fixHeight(y.parent)
            del y

        elif not L and R:  # R만 있음
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                y.right.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            self.fixHeight(y.parent)
            del y

        else:  # L도 R도 없음
            if pt == None:  # x가 루트노드인 경우
                self.root = None
            else:
                if pt.left is x:
                    pt.left = None
                else:
                    pt.right = None
                self.fixHeight(pt)
            del x
        self.size -= 1

    # 노드들의 height 정보 update 필요
    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        if x == None:
            return None
        r = x.right
        pt = x.parent
        if r:
            while r.left:
                r = r.left
            return r
        else:
            while pt != None and x == pt.right:
                x = pt
                pt = pt.parent
            return pt

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x is None:
            return None

        if x.left:
            if x.left.right:
                m = x.left.right
                while m.right:
                    m = m.right
                return m
            else:
                return x.left
        else:
            v = x
            if x.parent:
                x = x.parent
                while x:
                    if x.right:
                        if x.key < v.key:
                            return x
                    x = x.parent
        return None

    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        v = x.right
        if v == None:
            return
        b = v.left
        v.parent = x.parent
        if x.parent:
            if x.parent.right == x:
                x.parent.right = v
            else:
                x.parent.left = v
        v.left = x
        x.parent = v
        x.right = b
        if b:
            b.parent = x
        if x == self.root:
            self.root = v
        self.fixHeight(x)

    def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        v = x.left
        if v == None:
            return
        b = v.right
        v.parent = x.parent
        if x.parent != None:
            if x.parent.left == x:
                x.parent.left = v
            else:
                x.parent.right = v
        v.right = x
        x.parent = v
        x.left = b
        if b:
            b.parent = x
        if x == self.root:
            self.root = v
        self.fixHeight(x)


T = BST()
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
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
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
