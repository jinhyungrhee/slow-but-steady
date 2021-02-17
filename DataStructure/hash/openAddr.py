'''
H[i].key -> self.keys[i]
H[i].value -> self.values[i]
if H[i] is unoccupied: -> if self.keys[i] == None:
'''

class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size                # 해시 테이블의 슬롯 개수 = m
        self.keys = [None]*self.size    # 슬롯의 키를 저장하는 리스트(None means "unoccupied")
        self.values = [None]*self.size  # 슬롯의 값을 저장하는 리스트
    def __str__(self):
        s = ""
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
        while (self.keys[i] != None) and (self.keys[i] != key): # while문 탈출->1)내가 찾는 값이 없고 슬롯이 비어있다. 2)슬롯이 꽉 차있고 내가 찾던 값이 들어있다.
            i = (i + 1) % self.size # 한 바퀴 돌아서 다음으로 가게 만듦
            if i == start : return None # Full이면 None 리턴
        return i # 1)찾는 값이 없고 슬롯이 비어있으면 빈 슬롯 번호 리턴 2)찾던 값이 있으면 해당 슬롯 번호 리턴
    
    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None : return None # full이면 hash table의 크기를 키워야함
        elif self.keys[i] != None: # key가 테이블에 존재하면 (=key값이 테이블에 없지 않으면)
            self.values[i] = value # 해당 value update
        else:                      # key가 테이블에 없다면
            self.keys[i], self.values[i] = key, value # key와 value 삽입
        return key  # 성공적으로 연산 수행 확인

    def hash_function(self, key):
        return key % self.size

    def remove(self, key): # 삭제 연산 후 위치 조정 필요! (*중요*)
        i = self.find_slot(key)
        if self.keys[i] == None: return None # key가 존재하지 않을 경우 None 리턴
        j = i   # H[i] : 빈 슬롯, H[j] : 이사해야 할 슬롯
        while True: 
            self.keys[i], self.values[i] = None, None # H[i]를 빈 슬롯으로 만듦
            while True: # H[i]로 이사할 H[j] 찾기
                j = (j + 1) % self.size # 하나 아래로 내려가서 찾음
                if self.keys[j] == None: return key # 만약 H[j]가 빈칸이면 key값 리턴 = 자리 이동 완료!
                k = self.hash_function(self.keys[j]) 
                #|..i..k..j..|
                #|..j..i..k..| or |..k..j..i..| 이 경우에는 옮기면 안 됨!
                if not (i < k <= j or j < i < k or k <= j < i): break  # 이 조건이 만족하면 while loop를 빠져 나간 뒤,
            self.keys[i], self.values[i] = self.keys[j], self.values[j] # H[j]를 H[i]에 복사
            i = j
        
    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None: # key is in table
            return self.keys[i]  # (원래는 value를 리턴해야 함)
        else:  # key is not in table
            return None # not found!

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)

H = HashOpenAddr()
while True:
    cmd = input().split()
    if cmd[0] == 'set':
        key = H.set(int(cmd[1]))
        if key == None: print("* H is full!")
        else: print("+ {0} is set into H".format(cmd[1]))
    elif cmd[0] == 'search':
        key = H.search(int(cmd[1]))
        if key == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'remove':
        key = H.remove(int(cmd[1]))
        if key == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            print("- {0} is removed".format(cmd[1]))
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command, enter a proper command!")