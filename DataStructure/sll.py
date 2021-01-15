class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def pushFront(self, key):
        new_node = Node(key)
        new_node.next = L.head
        L.head = new_node
        L.size += 1

    def pushBack(self, key):
        v = Node(key)
        if len(self) == 0:
            self.head = v
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = v
        self.size += 1
            
    def popFront(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key 

    def popBack(self):
        if len(self) == 0 :
            return None
        else:
            #running technique
            prev, tail = None, self.head
            while tail != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key    

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    def __iter__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next

    def __str__(self):
        return "->".join(str(v) for v in L)

    def __len__(self):   
        return self.size

L = SinglyLinkedList()
L.pushFront(-1)
L.pushFront(9)
L.pushFront(3)
L.pushBack(10)
L.pushFront(7)
#L.popBack()

for x in L:
    print(x)

print(L)