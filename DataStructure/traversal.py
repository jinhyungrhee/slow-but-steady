class Node:
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.key)

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def preorder(self, v): # 노드 v와 자손 노드를 preorder로 방문하면서 출력
        if v != None:
            print(v.key)
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key)
            self.inorder(v.right)

    def postorder(self,v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key)


T = Tree()
a, b, c, d = Node(1), Node(2), Node(3), Node(4)
T.root = a
a.left = b
a.right = c
c.left = d
T.preorder(T.root)
T.inorder(T.root)
T.postorder(T.root)