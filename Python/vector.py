class Vector:
    def __init__(self, *args): # 여러 개의 매개 변수들을 tuple args를 통해 전달
        self._coords = list(args) # 좌표 값을 리스트 _coords(nonpublic변수)에 저장. [x for x in args]
                                  # nonpublic변수(private)는 이 클래스를 다른 곳에서 ipmort해 사용하는 경우 감춰짐.
    def __str__(self):
        return str(self._coords)

    def __len__(self): # return its dimension
        return len(self._coords)
    
    def __getitem__(self, k): # return the value of kth dimension
        return self._coords[k]

    def __setitem__(self, k, val): # return the value of kth dimension
        self._coords[k] = val
    
'''
__len__과 __getitem__ 메쏘드가 정의되면 해당 클래스에 대한 iterator가 자동으로 정의됨.
'''    

v = Vector(1, 2, 3)
v[-1] = 9

for c in v: 
    print(c, end=" ")
print()
print(len(v))
print(v[1])