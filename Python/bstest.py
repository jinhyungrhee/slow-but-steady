class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 노드x의 높이 / leaf == 0

    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v:
            print(v.key, end=" ")
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

    def find_loc(self, key):  # if key is in T, return its Node
        # if not in T, return the parent node under where it is inserted
        if self.size == 0:
            return None
        p = None  # p = parent node of v
        v = self.root
        while v:  # while v != None
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p  # 트리에 찾는 노드가 없으면 부모노드 리턴

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):  # height update - done!
        v = Node(key)  # 새 노드 생성
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)  # 방금 생성했으므로 부모노드p 리턴
            if p and p.key != key:  # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p

                if p.left == None or p.right == None:  # 두 자식 노드가 모두 찬 경우 제외
                    while p != None:  # height update
                        p.height += 1
                        p = p.parent  # ?
        '''
        while v.parent != None:  # height update
            if v.parent.right == None:
                v.parent.height += 1
            else:
                if v.parent.left.height > v.parent.right.height:
                    v.parent.height = v.parent.left.height + 1
                else:
                    v.parent.height = v.parent.right.height + 1
            v = v.parent
        '''
        self.size += 1
        return v

    def deleteByMerging(self, x):  # height update - 관련트리만 update
        # assume that x is not None
        a, b, pt = x.left, x.right, x.parent
        # c는 부트리 중 root노드 (x 대신 들어갈 노드)
        if a == None:  # 왼쪽 부트리가 없으면 - height 따로 처리 **
            c = b  # 오른쪽 부트리가 x 대체 (c == x노드 대체)
        else:  # a != None (a가 있으면 => a부트리에서 가장 큰 노드 올리기로 약속)
            c = m = a  # m 찾기 (a 부트리 중 가장 큰 노드)
            # find the largest leaf m in the subtree of a
            while m.right:
                m = m.right
            m.right = b  # 오른쪽 부트리(b)가 m의 오른쪽 자식이 됨 - 여기에서 H update?
            if b:  # b가 존재하면
                b.parent = m  # b의 부모는 m(a부트리 중 가장 큰 값)이 됨
                # b.height = 0

        if self.root == x:  # c becomes a new root (지우는 노드가 root인 경우)
            if c:
                c.parent = None
            self.root = c
        else:  # c becomes a child of pt of x (지우는 노드가 일반노드인 경우)
            if pt.left == x:  # 지우려는 노드가 왼쪽 자식노드일 때
                pt.left = c
            else:  # 지우려는 노드가 오른쪽 자식노드일 때
                pt.right = c
            if c:  # c가 존재하면
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

    def deleteByCopying(self, x):  # height update
        if x == None:
            return
        else:
            pt, L, R = x.parent, x.left, x.right
            if L:  # L이 있음
                y = x.left
                while y.right:  # m값 찾기
                    y = y.right  # y가 곧 m
                x.key = y.key  # m으로 x 대체
                if y.left:  # (x.left.left가 있다면) m의 left가 있다면
                    y.left.parent = y.parent  # m의 left의 부모를 m의 부모로 연결
                if y.parent.left is y:  # m이 왼쪽 자식 노드였다면
                    y.parent.left = y.left  # m 부모 왼쪽 자식노드에 m의 왼쪽 서브트리 붙임
                else:  # m이 오른쪽 자식 노드였다면
                    y.parent.right = y.left  # m 부모 오른쪽 자식노드에 m의 왼쪽 서브트리 붙임
                # height update - 해당 트리의 leaf노드 찾아서 처음부터 올라가기?
                # 어쨌든 m까지는 내려왔을 것(1-맨 왼쪽으로 더 내려가 leaf찾음 2-왼쪽이 없으면 본인이 leaf이므로 부모에서 시작)
                # leaf노드에서 올라가면서 비교해서 height update!
                # 내려갈 필요가 없는게 m 밑의 height값들은 바뀌지 않음 (위에 만 바뀐다)
                # 부모에게 내 height를 주고, 위로 올라가면서 비교하면서 값 update
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
                '''
                z = y.left
                if z == None:  # 자식노드가 없으면 본인만 올라감(경우에 따라 부모노드 height - 1)
                    y.height = x.height
                else:
                    while z.parent != None:
                        if z.parent.left == None:
                            z.parent.height = z.parent.right.height + 1
                        elif z.parent.right == None:
                            z.parent.height = z.parent.left.height + 1
                        else:
                            if z.parent.left.height > z.parent.right.height:
                                z.parent.height = z.parent.left.height + 1
                            else:
                                z.parent.height = z.parent.right.height + 1
                        z = z.parent
                '''
                del y

            elif not L and R:  # R만 있음(L없을 경우)
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
                # height update **
                # 어쨌든 m까지는 내려왔을 것(1-맨 오른쪽으로 더 내려가 leaf찾음 2-오른쪽이 없으면 본인이 leaf이므로 부모에서 시작)
                # leaf노드에서 올라가면서 비교해서 height update!
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
                '''
                z = y.right
                if z == None:
                    y.height = x.height
                else:
                    while z.parent != None:
                        if z.parent.left == None:
                            z.parent.height = z.parent.right.height + 1
                        elif z.parent.right == None:
                            z.parent.height = z.parent.left.height + 1
                        else:
                            if z.parent.left.height > z.parent.right.height:
                                z.parent.height = z.parent.left.height + 1
                            else:
                                z.parent.height = z.parent.right.height + 1
                        z = z.parent
                '''
                del y

            else:  # L도 R도 없음
                if pt == None:  # x가 루트노드인 경우
                    self.root = None
                else:  # 리프노드인 경우 - 부모ㅢ height 줄여아 하나?(일단 보류)
                    if pt.left is x:
                        pt.left = None
                    else:
                        pt.right = None
                del x

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def succ(self, x):
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

    def pred(self, x):  # 이전노드 찾기
        l, r, pt = x.left, x.right, x.parent
        if l == None:  # 왼쪽 자식 노드가 없으면
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

    def rotateRight(self, x):  # height 수정하기
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
        if b == None:  # 추가
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

    def rotateLeft(self, x):
        z = x.right  # x != None이라고 가정
        if z == None:
            return  # 오른쪽 subtree를 돌려야 하는데 없으므로 할 수 없음
        b = z.left  # b subtree(왼쪽subtree) 떼어내서 다른 곳에 붙임
        z.parent = x.parent  # x건너 뛰어서 연결
        if x.parent:  # x가 루트노드가 아니면
            if x.parent.right == x:
                x.parent.right = z
            else:
                x.parent.left = z
        if z:
            z.left = x  # x가 z의 왼쪽 자식트리로 내려감(rotate)
        x.parent = z  # 부모-자식 관계 바뀜
        x.right = b
        if b:  # b != None
            b.parent = x
        # x == self.root라면 z가 새로운 루트가 되어야 함
        if x == self.root and x != None:
            self.root = z
        if b == None:
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


T = Tree()
# T.insert(5)  # 맨처음 insert한게 root가 됨. root를 기준으로 좌우 결정
# T.insert(3)
# T.insert(1)
T.insert(5)
T.insert(3)
T.insert(20)
T.insert(10)
T.insert(25)
T.insert(18)
T.insert(17)
T.insert(15)
T.insert(19)

# T.inorder(T.search(5))
# print()
T.preorder(T.root)
# T.deleteByMerging(T.search(18))
# print()
# T.postorder(T.root)
print()
# print(T.succ(T.search(25)))
# print(T.pred(T.search(18)))
T.deleteByCopying(T.search(1))
T.preorder(T.root)  # MLR
print()
# T.inorder(T.root)  # LMR
print()
print(T.height(T.search(5)))
print(T.height(T.search(3)))
print(T.height(T.search(20)))
print(T.height(T.search(10)))
print(T.height(T.search(25)))
print(T.height(T.search(18)))
print(T.height(T.search(17)))
print(T.height(T.search(19)))
print(T.height(T.search(15)))


# T.rotateRight(T.search(5))  # root노드일 경우 부모의 왼쪽 오른쪽이 없음 -따로 처리 필요
# T.rotateRight(T.search(5))
# T.rotateLeft(T.search(10))  # 노드가 없을 경우 에러 발생 - 처리 필요
T.preorder(T.root)
# T.rotateLeft(T.search(20))
T.rotateRight(T.search(20))
print()
print(T.height(T.search(5)))
print(T.height(T.search(3)))
print(T.height(T.search(20)))
print(T.height(T.search(10)))
print(T.height(T.search(25)))
print(T.height(T.search(18)))
print(T.height(T.search(17)))
print(T.height(T.search(19)))
print(T.height(T.search(15)))
'''
print(T.height(T.search(5)))
print(T.height(T.search(3)))
print(T.height(T.search(20)))
print(T.height(T.search(25)))
print(T.height(T.search(10)))
print(T.height(T.search(18)))
print(T.height(T.search(17)))
'''

'''
B = Tree()
B.insert(3)  # root / height = 2
B.insert(7)  # right of root / height = 1
B.insert(1)  # left of root / height = 1
B.insert(2)  # right of node(1) / height = 2
B.insert(0)  # left of node(1) / height = 2
B.inorder(B.root)
'''
