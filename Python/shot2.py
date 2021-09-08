class HashOpenAddr:
    def __init__(self, size):  # input size는 1~100,000까지
        self.size = size
        self.keys = [None]*self.size  # item #
        self.values = [None]*self.size  # frequency

    def __str__(self):
        s = " "
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]  # self.keys[i] or self.values[i] ?

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        # while문 탈출 조건: 1)내가 찾는 값이 없고 비어있음(slot번호 리턴) 2)꽉 차있고 내가 찾던 값이 들어있음
        while (self.keys[i] != None) and (self.keys[i] != key):
            i = (i + 1) % self.size  # 한 바퀴 돌아서 다음으로 감
            if i == start:
                return None  # FUll
        return i  # 1) 찾는 값이 없고 비어있으면 빈 슬롯 번호 리턴 2) 찾던 값이 있으면 해당 슬롯 번호 리턴

    def set(self, key, value=None):  # set1 과 set2를 만들까?
        i = self.find_slot(key)
        if i == None:
            return None  # Full이면 Hash Table의 크기를 키워야 함(나중에)
        elif self.keys[i] != None:  # key가 테이블에 존재하면
            # self.values[i] = value  # 해당 value update
            start = i
            while (self.keys[i] != None):
                i = (i + 1) % self.size  # 다음칸으로
                if i == start:
                    return None  # Full - do somethig?
            self.keys[i] = key
        else:  # key가 테이블에 없으면
            self.keys[i], self.values[i] = key, value  # key와 value 삽입
        return key

    def set2(self, key, value=None):  # set1 과 set2를 만들까?
        i = self.find_slot(key)
        if i == None:
            return None  # Full이면 Hash Table의 크기를 키워야 함(나중에)
        elif self.keys[i] != None:  # key가 테이블에 존재하면
            self.values[i] = value  # 해당 value update
        else:  # key가 테이블에 없으면
            self.keys[i], self.values[i] = key, value  # key와 value 삽입
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):  # 삭제 후 필요하면 한칸씩 당김!
        i = self.find_slot(key)
        if self.keys[i] == None:
            return None  # key가 없을 경우
        j = i  # H[i] : 빈 슬롯, H[j] : 이사해야 할 슬롯
        while True:
            self.keys[i], self.values[i] = None, None  # H[i]를 빈 슬롯으로 만듦
            while True:  # **H[i]로 이사할 H[j] 찾기!**
                j = (j + 1) % self.size  # 하나 아래로 내려가서 찾음
                if self.keys[j] == None:  # 만약 H[j]가 빈칸이면 key값 리턴
                    return key
                k = self.hash_function(self.keys[j])
                # if not (i < k <= j or j < i < k or k <= j < i):
                if not (i < k <= j or j < i < k or k <= j < i):
                    break  # 이 조건들에 해당하면 break
            self.keys[i], self.values[i] = self.keys[j], self.values[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:  # key is in table
            return self.values[i]  # values(frequency)리턴 = 몇개가 중복해서 있는지 파악 가능
        else:  # key is not in table
            return None

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)


A = [int(x) for x in input().split()]  # 명수 물건 번호
B = [int(x) for x in input().split()]  # 재석 물건 번호

#A = [4, 8, 7, 4, 1, 4, 1]
#B = [2, 1, 3, 4, 1, 4, 4]

H = HashOpenAddr(int(len(A)*1.5))  # 동일한 값 찾는 hash table
# H2 = HashOpenAddr(int(len(A)*1.5))  # 중복된 값 없애는 hash table
'''
for x in A:
    H.set(x)  # 함수 set()은 똑같은 key값이 이미 존재하면 한칸 아래로 내려가서 key값 저장(open addressing 방법)

print(H)
print()
for i in B:
    if H.search(i) != None:
        print(i, end=" ")
        H2.set2(i)  # 함수 set2()는 똑같은 key값이 이미 존재하면 덮어씌움(중복된 값 X)
        H.remove(i)
    else:
        pass
print()
print(H)
print(H2)

print()
for i in B:  # 여기를 고쳐볼까
    if H2.search(i) != None:
        print(i, end=" ")
        H2.remove(i)
    else:
        pass
'''
for i in B:
    if i in A:
        x = H.search(i)
        if x == None:  # 존재하는 key가 없으면
            H.set2(i, 1)
            print(i, end=" ")
            A.remove(i)
        else:
            H.set2(i, x+1)
            print(i, end=" ")
            A.remove(i)
        #
        #H.set2(i, 1)
print()
print(H)
print(B)
'''
for i in H:
    if i != None:
        print(i, end=" ")
'''
'''
for i in B:
    x = H.search(i)  # value(frequency)값 리턴 2-1개, 1-2개
    H2.set2(i, 1)
    H.set2(i, x-1)
    print(i, end=" ")

print(H2)
'''
for i in B:  # remove를 쓰지 않는 방법?
    if H.search(i) != None:
        print(i, end=" ")
        H.remove(i)
    else:
        pass
print(H)
