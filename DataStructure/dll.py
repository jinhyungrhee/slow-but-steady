class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = self
        self.prev = self
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

    def __str__(self):
        return "->".join(str(v) for v in L)

    def __len__(self):
        return self.size

    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return

        ap = a.prev # ap is previous node of a
        bn = b.next # bn is next node of b
        
        # cut [a..b]
        ap.next = bn
        bn.prev = ap

        # insert [a..b] after x
        xn = x.next
        xn.prev = b
        b.next = xn
        a.prev = x
        x.next = a
        
    def moveAfter(self, a, x):
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def remove(self, x):
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x

    def search(self, key):
        v = self.head # dummy node
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

L = DoublyLinkedList()
L.pushFront(5)
L.pushBack(7)
