class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

    def __iter__(self):  # error
        return self.parent.__iter__()    

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0 # 필요하다면 높이 정보 저장

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    
    def __str__(self): # 한방향리스트 _str_와 유사 정의
        return " - ".join(str(k) for k in self)

    def preorder(self, v): # MLR
        if v != None:
            print(v.key)
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v): # LMR
        if v != None:
            self.inorder(v.left)
            print(v.key)
            self.inorder(v.right)

    def postorder(self, v): # LRM
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key)

    def find_loc(self, key): # key값 노드가 있으면 해당 노드 return, 없으면 노드가 삽입될 부모노드 return
        if self.size == 0: return None
        p = None    # p is parent of v
        v = self.root
        while v: # leaf 노드까지 검색
            if v.key == key: return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p # key값이 tree에 속하지 않으면 부모노드 return

    def search(self, key):
        v = self.find_loc(key)
        if v and v.key == key:  # key is in tree
            return v
        else: 
            return None

    def insert(self, key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None: # root노드인 경우
                self.root = v # v를 self의 root로 설정
            else: ###
                v.parent = p
                if p.key >= key: #check if left/right
                    p.left = v
                else:
                    p.right = v
            self.size += 1  # size 1 증가
            return v        # 새로 삽입된 노드(v)리턴 => 다른 연산에 사용 가능
        else: ###
            print("key is already in tree!")
            return p # 중복 key를 허용하지 않으면 None 리턴
    
#    def deleteByMerging 
#    def deleteByCopying

T = BST()
T.insert(15)
T.insert(4)
print(T.__len__())
T.insert(7)
print(T.__len__())
#print(T.__iter__())
print(T.search(15))
T.insert(2)
T.insert(6)
print(T.__len__())