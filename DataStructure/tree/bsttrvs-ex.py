'''
이진탐색트리(Binary Search Tree, BST)
- 각 노드의 왼쪽 sub tree의 key값은 노드의 key값보다 작거나 같아야 하고
- 각 노드의 오른쪽 sub tree의 key값은 노드의 key값보다 커야 한다.
'''

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

    def preorder(self, v): # 노드v와 자손노드를 preorder(MLR)로 방문하면서 출력 (재귀)
        if v != None:
            print(v.key, end=" ") # (end=" ")를 추가하면 '\n' 없이 한 줄로 출력!
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v): # LMR 순서로 방문
        if v != None:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v): #LRM순서로 방문
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=" ")

    def find_loc(self, key): # key값 노드가 있으면 해당노드 리턴, 없으면 부모노드 리턴
        if self.size == 0: return None # 빈 리스트
        p = None # p is parent of v
        v = self.root 
        while v: # root에서 leaf노드까지 검색 (값을 비교하면서 계속 타고 내려감)
            if v.key == key: return v # 찾는 값이 v값이면 [=> 계속 while loop를 돌다가 찾는 값이 있으면 해당 값 return]
            elif v.key < key: # 찾는 값이 v값보다 크면 
                p = v
                v = v.right
            else: # 찾는 값이 v값보다 작으면
                p = v
                v = v.left
        return p # [=>key 값이 tree에 없으면 부모노드 리턴/ 부모노드도 없으면(=root노드이면) None리턴]

    def search(self, key):
        v = self.find_loc(key) 
        if v and v.key == key: # v가 tree에 있고 v의 key값이 찾는 key값과 같으면
            return v
        else:
            return None

    def insert(self, key): # key가 이미 트리에 있다면 에러 출력 없이 None만 리턴!
        p = self.find_loc(key) # key 노드가 있으면 해당노드 리턴, 없으면 부모노드 리턴
        if p == None or p.key != key: # <1>: 찾는 값이 없음 -> tree에 추가
            v = Node(key) # 추가할 노드 생성
            if p == None: # <1>-1: 값이 부모노드(root노드)에 삽입되어야 하는 경우 *?* 
                self.root = v # v를 root노드로 설정
            else: # <1>-2: 값이 자식노드에 삽입되어야 하는 경우 *?*
                v.parent = p
                if p.key >= key: # 삽입할 값이 부모의 값보다 작거나 같으면
                    p.left = v # 왼쪽 자식노드로 들어감
                else: # 삽입할 값이 부모의 값보다 크면
                    p.right = v # 오른쪽 자식노드로 들어감
            self.size += 1
            return v # 새로 삽입된 노드 리턴 => 다른 연산에 사용!
        else: # <2>: 찾는 값이 있음 -> None 리턴
            return None # find_loc에서 값이 없으면 None

T = Tree()

while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        if v != None:
            print("+ {0} is set into H".format(v.key))
        else:
            print("* {0} is already in the tree!".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root) # **root에 대해서 traversal**
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
    
