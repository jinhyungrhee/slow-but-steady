'''
21.03.19 실습 수업 내용
'''
'''
def f(*argv):  # 몇개의 arg가 들어오든 하나의 tuple로 묶어내는 역할 => * // 정해지지 않은 파라미터를 받을 수 있음
    argv[0]

def __init__(self, *args):
    self._coords = list(args) # 내부 메서드 안에서만 다루고 싶을 때 _coords (언더바 하나) 사용 => protected // (언더바 두개) => private

lit = [1, 2, 3]

len(lit)
lit[0]

print("가나다", "abc", "123")
'''

capacity = 2
A = [1, 2]
B = [None] * 5
print(B)
for i in range(capacity):
    B[i] = A[i]

'''
try:
    print(A[4])
except:
    print("IndexError")
'''

if not A[4]:
    print("IndexError")
else:
    print(A[4]) 