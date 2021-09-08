class myList():
    def __init__(self): 
        self.capacity = 2   # myList의 용량 (저장할 수 있는 원소 개수)
        self.n = 0          # 실제 저장된 값의 개수
        self.A = [None] * self.capacity # 실제 저장 자료 구조(Python리스트)

    def __len__(self):
        return self.n

    def __str__(self):
        return f'   ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

    def size(self):
        return self.n

    def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if k < 0 and k >= -(self.n):
            return self.A[self.n + k]
        elif k >= 0 and k < self.n:
            return self.A[k]
        else:
            raise IndexError
    
    def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		# k가 음수일 수도 있음
		# k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if k < 0 and k >= -(self.n):
            self.A[self.n + k] = x
        elif k >= 0 and k < self.n:
            self.A[k] = x
        else:
            raise IndexError

    def change_size(self, new_capacity):
        print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
	    # 1. new_capacity의 크기의 리스트 B를 만듬
	    # 2. self.A의 값을 B로 옮김
	    # 3. del self.A  (A 지움)
	    # 4. self.A = B
	    # 5. self.capacity = new_capacity
        B = [None] * new_capacity # new_capacity = 5이면,  [None, None, None, None, None]
        for i in range(self.capacity): #self.A의 원소 B로 옮김
            B[i] = self.A[i]
        self.A.clear()
        self.A = B
        self.capacity = new_capacity
        

    def append(self, x):
        if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
            self.change_size(self.capacity*2)
            self.A[self.n] = x      # 맨 뒤에 삽입
            self.n += 1             # n 값 1 증가
        else:
            self.A[self.n] = x      # 맨 뒤에 삽입
            self.n += 1             # n 값 1 증가

    
    def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
        if self.n == 0: # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: (음수도 처리해줘야함..ㅠㅠ)
            raise IndexError
        elif self.capacity >= 4 and self.n <= self.capacity//4 : # 실제 key값이 전체의 25%이하면 halving
            self.change_size(self.capacity//2)
        # 1. k값이 주어진 경우와 주어지지 않은 경우를 구별해야 함
        # 2. x = self.A[k]
        # 3. A[k]와 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
        # 4. self.n -= 1
        # 5. return x
        if k == None:                   # try - except를 써서 인덱스 범위 바깥 부분을 except 처리하면 될듯?
            x = self.A[self.n-1]
            self.A[self.n-1] = None
            self.n -= 1
            return x
        elif k >= 0 and k < self.n:
            x = self.A[k] 
            self.A[k] = None
            for i in range(k, self.n-1): # A[k]와 오른쪽 값들이 한 칸씩 왼쪽으로 이동해 메꿈
                self.A[i] = self.A[i+1]
            self.n -= 1
            return x
        elif k < 0 and k >= -(self.n):
            x = self.A[self.n + k]   
            self.A[self.n + k] = None
            for i in range(self.n+k, self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
            return x
        else:
            raise IndexError

    def insert(self, k, x):
        # 주의 : k 값이 음수값일 수도 있음
        # k 값이 올바른 인덱스 범위를 벗어나면 , raise IndexError
        # 1. k의 범위가 올바르지 않다면 IndexError 발생시킴
        # 2. self.n == self.capacity이면 self.changing_size(self.capacity*2) 호출해 doubling
        # 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
        # 4. self.A[k] = x
        # 5. self.n += 1
        if k < 0 and k >= -(self.n): # k값이 음수일 때
            if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
                self.change_size(self.capacity*2)
            for i in range(self.n-1, self.n+k-1, -1): # k = -2이면
                self.A[i+1] = self.A[i]
            self.A[self.n+k] = x
            self.n += 1
        elif k >= 0 and k < self.n: # k가 인덱스를 벗어나지 않는 양수일때
            if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
                self.change_size(self.capacity*2)
            for i in range(self.n-1, k-1, -1):
                self.A[i+1] = self.A[i]
            self.A[k] = x
            self.n += 1
        else:
            raise IndexError

L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get': # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set': # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")
