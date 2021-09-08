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
                '''
                if p.left == None or p.right == None:  # 두 자식 노드가 모두 찬 경우 제외
                    while p != None:  # height update
                        p.height += 1
                        p = p.parent
                '''
                # update height - v.parent == p (맞는거 같은데 왜 오류발생?)
                while p != None:
                    if p.left == None:
                        p.height = p.right.height + 1
                    elif p.right == None:
                        p.height = p.left.height + 1
                    else:  # 둘 다 있으면 비교
                        if p.left.height > p.right.height:
                            p.height = p.left.height + 1
                        else:
                            p.height = p.right.height + 1
                    # b.parent.height += 1
                    p = p.parent  # 하나 더 위의 부모로 올라감
        self.size += 1
        return v

    def deleteByMerging(self, x):
        if x == None:
            return None
        else:
            # 노드들의 height 정보 update 필요
            # assume that x is not None
            a, b, pt = x.left, x.right, x.parent

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
            # height update
            # 초기에 b가 삽입되었을 때 조건 판단
            while b.parent != None:  # 일단 b는 무조건 m이나 pt의 오른쪽 자식으로 붙는다 **
                # 오른쪽 자식 왼쪽 자식 height 비교해서 더 높은 값에 +1
                # 경우의 수 - 1)왼쪽 자식노드만 없거나, 2)왼쪽 자식노드도 있거나 - 비교 어떻게?
                if b.parent.left == None:
                    b.parent.height = b.parent.right.height + 1
                elif b.parent.right == None:
                    b.parent.height = b.parent.left.height + 1
                else:  # 둘 다 있으면 비교
                    if b.parent.left.height > b.parent.right.height:
                        b.parent.height = b.parent.left.height + 1
                    else:
                        b.parent.height = b.parent.right.height + 1
                # b.parent.height += 1
                b = b.parent  # 하나 더 위의 부모로 올라감

    def deleteByCopying(self, x):
        if x == None:  # x로 부모노드가 리턴될 수 도 있음. 부모노드도 안됨
            return None
        else:
            # 노드들의 height 정보 update 필요
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
                # height update
                y.height += -1  # 내 값에서 -1을 하고 비교를 하면 부모의 h 값이 내 값이 됨
                while y.parent != None:  # 일단 b는 무조건 m이나 pt의 오른쪽 자식으로 붙는다 **
                    # 오른쪽 자식 왼쪽 자식 height 비교해서 더 높은 값에 +1
                    # 경우의 수 - 1)왼쪽 자식노드만 없거나, 2)왼쪽 자식노드도 있거나 - 비교 어떻게?
                    if y.parent.left == None and y.parent.right == None:
                        y.parent.height = 0
                    else:
                        if y.parent.left == None:
                            y.parent.height = y.parent.right.height + 1
                        elif y.parent.right == None:
                            y.parent.height = y.parent.left.height + 1
                        else:  # 둘 다 있으면 비교
                            if y.parent.left.height > y.parent.right.height:
                                y.parent.height = y.parent.left.height + 1
                            else:
                                y.parent.height = y.parent.right.height + 1
                    # b.parent.height += 1
                    y = y.parent  # 하나 더 위의 부모로 올라감
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
                # height update
                y.height += -1  # 내 값에서 -1을 하고 비교를 하면 부모의 h 값이 내 값이 됨
                while y.parent != None:  # 일단 b는 무조건 m이나 pt의 오른쪽 자식으로 붙는다 **
                    # 오른쪽 자식 왼쪽 자식 height 비교해서 더 높은 값에 +1
                    # 경우의 수 - 1)왼쪽 자식노드만 없거나, 2)왼쪽 자식노드도 있거나 - 비교 어떻게?
                    if y.parent.left == None and y.parent.right == None:
                        y.parent.height = 0
                    else:
                        if y.parent.left == None:
                            y.parent.height = y.parent.right.height + 1
                        elif y.parent.right == None:
                            y.parent.height = y.parent.left.height + 1
                        else:  # 둘 다 있으면 비교
                            if y.parent.left.height > y.parent.right.height:
                                y.parent.height = y.parent.left.height + 1
                            else:
                                y.parent.height = y.parent.right.height + 1
                    # b.parent.height += 1
                    y = y.parent  # 하나 더 위의 부모로 올라감
                del y

            else:  # L도 R도 없음 - x 루트노드거나 리프노드
                if pt == None:  # x가 루트노드인 경우
                    self.root = None
                else:
                    if pt.left is x:  # x가 왼쪽 자식이면
                        pt.left = None
                    else:  # x가 오른쪽 자식이면
                        pt.right = None
                del x
                while pt != None:  # 리프노드 삭제시 height update
                    if pt.left == None and pt.right == None:
                        pt.height = 0
                    else:
                        if pt.left == None:
                            pt.height = pt.right.height + 1
                        elif pt.right == None:
                            pt.height = pt.left.height + 1
                        else:  # 둘 다 있으면 비교
                            if pt.left.height > pt.right.height:
                                pt.height = pt.left.height + 1
                            else:
                                pt.height = pt.right.height + 1
                    # b.parent.height += 1
                    pt = pt.parent  # 하나 더 위의 부모로 올라감

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
            l, r, pt = x.left, x.right, x.parent
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
            return
        else:
            # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
            l, r, pt = x.left, x.right, x.parent
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
        # update height
        if x.left == None:  # x.left == None인 경우 - x가 내려가면서 x.height == 0이됨
            x.height = 0  # z의 height는 변하지 않음 - 내려간 x와 z의 부모 height만 바뀜
            while z.parent != None:
                if z.parent.left == None:
                    z.parent.height = z.parent.right.height + 1
                elif z.parent.right == None:
                    z.parent.height = z.parent.left.height + 1
                else:  # 둘 다 있으면 비교
                    if z.parent.left.height > z.parent.right.height:
                        z.parent.height = z.parent.left.height + 1
                    else:
                        z.parent.height = z.parent.right.height + 1
                z = z.parent  # 하나 더 위의 부모로 올라감
        elif b == None:  # 잘못된 듯?
            z.height = x.height + 1
        else:
            while b.parent != None:
                if b.parent.left == None:
                    b.parent.height = b.parent.right.height + 1
                elif b.parent.right == None:
                    b.parent.height = b.parent.left.height + 1
                else:  # 둘 다 있으면 비교
                    if b.parent.left.height > b.parent.right.height:
                        b.parent.height = b.parent.left.height + 1
                    else:
                        b.parent.height = b.parent.right.height + 1
                b = b.parent  # 하나 더 위의 부모로 올라감

    def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
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
        # update height
        if x.right == None:  # x.left == None인 경우 - x가 내려가면서 x.height == 0이됨
            x.height = 0  # z의 height는 변하지 않음 - 내려간 x와 z의 부모 height만 바뀜
            while z.parent != None:
                if z.parent.left == None:
                    z.parent.height = z.parent.right.height + 1
                elif z.parent.right == None:
                    z.parent.height = z.parent.left.height + 1
                else:  # 둘 다 있으면 비교
                    if z.parent.left.height > z.parent.right.height:
                        z.parent.height = z.parent.left.height + 1
                    else:
                        z.parent.height = z.parent.right.height + 1
                z = z.parent  # 하나 더 위의 부모로 올라감
        elif b == None:
            z.height = x.height + 1
        else:
            while b.parent != None:
                if b.parent.left == None:
                    b.parent.height = b.parent.right.height + 1
                elif b.parent.right == None:
                    b.parent.height = b.parent.left.height + 1
                else:  # 둘 다 있으면 비교
                    if b.parent.left.height > b.parent.right.height:
                        b.parent.height = b.parent.left.height + 1
                    else:
                        b.parent.height = b.parent.right.height + 1
                b = b.parent  # 하나 더 위의 부모로 올라감


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
