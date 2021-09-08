class Node:
    # 정의 필요
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)


class BST:
    # 정의 필요
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
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

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None  # p = parent node of v
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

    def fixHeight(self, x):  # x의 왼쪽, 오른쪽을 비교해 x부터 root까지 height부여
        while x:
            if x.left == None and x.right == None:  # x의 자식 없는 경우
                x.height = 0
            elif x.left != None and x.right == None:  # x의 왼쪽만 있는 경우
                x.height = x.left.height + 1
            elif x.left == None and x.right != None:  # x의 오른쪽만 있는 경우
                x.height = x.right.height + 1
            else:  # 왼, 오 둘 다 있을 땐 큰 쪽을 따라감
                if x.left.height > x.right.height:
                    x.height = x.left.height + 1
                else:
                    x.height = x.right.height + 1
            x = x.parent
        return

    def insert(self, key):
        # 노드들의 height 정보 update 필요
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

    def deleteByMerging(self, x):
        if x == None:
            return None
        else:
            # 노드들의 height 정보 update 필요
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

            if m:  # m이 있으면
                self.fixHeight(m)
            else:  # m이 없으면
                self.fixHeight(pt)

    def deleteByCopying(self, x):
        if x == None:
            return None
        pt, L, R = x.parent, x.left, x.right
        if L:  # L이 있음
            y = x.left
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
            s = y.parent  # added
            del y
            return s  # added

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
            s = y.parent  # added
            del y
            return s  # added

        else:  # L도 R도 없음 - x 루트노드거나 리프노드
            if pt == None:  # x가 루트노드인 경우
                self.root = None
            else:
                if pt.left is x:  # x가 왼쪽 자식이면
                    pt.left = None
                else:  # x가 오른쪽 자식이면
                    pt.right = None
                self.fixHeight(pt)
                return pt  # added
            del x
        self.size -= 1

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        if x == None:
            return
        else:
            # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
            r, pt = x.right, x.parent
            # 자기보다 큰 값을 만날때까지 부모와 비교하며 계속 올라감
            if r == None:  # 오른쪽 자식노드 x, 왼쪽 자식노드만 있음
                while pt.key < x.key:  # 부모의 값이 나보다 클 때까지 올라감
                    pt = pt.parent
                    if pt == None:  # 가장 큰 값
                        return None
                return pt  # 큰 게 나오면 내 다음 값임
            else:
                c = x.right  # 오른쪽 자식노드로 내려감
                if c.left == None:  # 오른쪽 자식의 왼쪽 자식이 없으면 걔
                    return c
                else:  # 오른쪽 자식의 왼쪽이 있으면 왼쪽 끝까지 타고 내려감
                    while c.left.left != None:
                        c.left = c.left.left  # 가능?
                    return c.left

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        if x == None:
            return None
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        l, pt = x.left, x.parent
        if l == None:  # 왼쪽 자식 노드가 없으면
            if pt == None:
                return None
            while pt.key > x.key:  # 부모의 값이 내 값보다 작아질 때까지
                pt = pt.parent
                if pt == None:  # 가장 작은 값
                    return None
            return pt  # 작은 게 나오면 내 전 값임
        else:  # 왼쪽 자식 노드가 있으면
            c = x.left  # 왼쪽 자식노드로 내려감
            if c.right == None:
                return c
            else:  # 왼쪽 자식의 오른쪽 자식이 있으면 끝까지 타고 내려감
                while c.right.right != None:
                    c.right = c.right.right
                return c.right

    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        z = x.right  # x != None이라고 가정
        if z == None:
            return  # 오른쪽 subtree를 돌려야 하는데 없으므로 할 수 없음
        b = z.left  # b subtree(왼쪽subtree) 떼어내서 다른 곳에 붙임
        z.parent = x.parent  # x건너 뛰어서 연결
        if x.parent:  # x가 루트노드가 아니면
            if x.parent.right == x:
                x.parent.right = z
            else:
                x.parent.left = z  # 이 지점부터 위로 올라가며 hegiht update!
        if z:
            z.left = x  # x가 z의 왼쪽 자식트리로 내려감(rotate) # 여기서 x의 위치 바뀜
        x.parent = z  # 부모-자식 관계 바뀜 # 이 지점부터 위로 올라가며 hegiht update!
        x.right = b
        if b:  # b != None
            b.parent = x
        # x == self.root라면 z가 새로운 루트가 되어야 함
        if x == self.root and x != None:
            self.root = z
        self.fixHeight(x)

    def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        z = x.left  # x != None 이라고 가정
        if z == None:
            return  # z == None이면 아무것도 바뀌지 않음
        b = z.right  # b subtree를 떼어내서 다른 곳에 붙여야함
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        if z:
            z.right = x
        x.parent = z
        x.left = b
        if b:
            b.parent = x
        # x == self.root라면 z가 새로운 루트가 되어야 함
        if x == self.root and x != None:
            self.root = z
        self.fixHeight(x)


class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def rebalance(self, x, y, z):
        # assure that x, y, z != None
        # return the new 'top' node after rotations
        # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음
        if x == None or y == None or z == None:
            return
        if z.left == y and y.left == x:  # linear - 1회 로테이션
            super(AVL, self).rotateRight(z)
            return y
        elif z.right == y and y.right == x:
            super(AVL, self).rotateLeft(z)
            return y
        elif z.left == y and y.right == x:  # triangle - 2회 로테이션
            super(AVL, self).rotateLeft(y)
            super(AVL, self).rotateRight(z)
            return x
        elif z.right == y and y.left == x:
            super(AVL, self).rotateRight(y)
            super(AVL, self).rotateLeft(z)
            return x

    def insert(self, key):
        # BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면
        # super(class_name, instance_name).method()으로 호출
        # 새로 삽입된 노드가 리턴됨에 유의!
        v = super(AVL, self).insert(key)
        # x, y, z를 찾아 rebalance(x, y, z)를 호출 - v에서 위로 올라가며 x,y,z 찾음
        z, y, x = v.parent, v, None
        while z != None:  # avl조건이 깨질때까지 위로 올라감
            #            if z.left == None or z.right == None:
            #                x = y
            #                y = y.parent
            #                z = z.parent
            #            else:
            if abs(self.height(z.left) - self.height(z.right)) > 1:  # 깨지면 break
                break
#                    w = self.rebalance(x, y, z)  # w는 새로 z 자리에 올라온 노드
#                    if w.parent == None:  # 새로운 z노드인 w가 root면 root정보 update!
#                        self.root = w
            x = y
            y = y.parent
            z = z.parent  # 깨지지 않으면?
        if z != None and y != None and x != None:
            w = self.rebalance(x, y, z)  # w는 새로 z 자리에 올라온 노드
            if w.parent == None:  # 새로운 z노드인 w가 root면 root정보 update!
                self.root = w
        return v

    def delete(self, u):  # delete the node u
        # 또는 self.deleteByMerging을 호출가능하다. 그러나 이 과제에서는 deleteByCopying으로 호출한다
        v = self.deleteByCopying(u)
        # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장 (일반적으로 parent?)

        while v:  # v가 none이 아닐 동안
            # v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
            # z - y - x를 정한 후, rebalance(x, y, z)을 호출
            if abs(self.height(v.left) - self.height(v.right)) > 1:  # 조건이 깨졌으면(v is not balanced)
                z = v
                if self.height(z.left) >= self.height(z.right):  # 왼쪽이 더 무거우면
                    y = z.left  # y는 왼쪽 자식
                else:  # 오른쪽이 더 무거우면
                    y = z.right  # y는 오른쪽 자식
                if self.height(y.left) >= self.height(y.right):  # y의 왼쪽이 더 무거우면
                    x = y.left  # x는 왼쪽 자식
                else:  # y의 오른쪽이 더 무거우면
                    x = y.right  # x는 오른쪽 자식
                v = self.rebalance(x, y, z)
            w = v  # w는 하나 밑에서 따라감 (w는 이전의 v노드)
            v = v.parent
        self.root = w  # v가 none이 되면 while루프 빠져나옴 -> 그때 w가 root노드가 됨


T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
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
