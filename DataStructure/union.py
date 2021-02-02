class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0

def make_set(x):
    return Node(x)

def find(x):    # x의 root 리턴
    while x.parent != x:
        x = x.parent
    return x
    
def union(x, y):
    v, w = find(x), find(y)
    if v.rank > w.rank:
        v, w = w, v
    v.parent = w
    if v.rank == w.rank:
        w.rank += 1

a = make_set(1)
b = make_set(2)
c = make_set(3)
d = make_set(4)
e = make_set(5)
union(a,b)
union(a,c)
union(d,e)
union(c,d)