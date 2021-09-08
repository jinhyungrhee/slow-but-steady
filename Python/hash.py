class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

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
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        # while문 탈출 조건: 1)내가 찾는 값이 없고 비어있음(slot번호 리턴) 2)꽉 차있고 내가 찾던 값이 들어있음
        while (self.keys[i] != None) and (self.keys[i] != key):
            i = (i + 1) % self.size  # 한 바퀴 돌아서 다음으로 감
            if i == start:
                return None  # FUll
        return i  # 1) 찾는 값이 없고 비어있으면 빈 슬롯 번호 리턴 2) 찾던 값이 있으면 해당 슬롯 번호 리턴

    def set(self, key, value=None):
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
                if not (i < k <= j or j < i < k or k <= j < i):
                    break  # 이 조건들에 해당하면 break
            self.keys[i], self.values[i] = self.keys[j], self.values[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:  # key is in table
            return self.keys[i]
        else:  # key is not in table
            return None  # not found

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)


A = [int(x) for x in input().split()]  # 명수 물건 번호
# B = [int(x) for x in input().split()]  # 재석 물건 번호
print(A)
H = HashOpenAddr()
#JH = HashOpenAddr()
for i in A:
    H.set(i)
print(H)
