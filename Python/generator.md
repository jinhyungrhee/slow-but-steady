# 이터레이터(Iterator)

- 파이썬에서 반복자는 여러 개의 요소를 가지는 **컨테이너(리스트, 튜플, 셋, 딕셔너리, 문자열)**에서 각 요소를 하나씩 꺼내 어떤 처리를 수행하는 간편한 방법을 제공하는 객체.  
- literable type:
    - list
    - tuple
    - set
    - keys of dict
    - characters of string
    - lines of file  

```py
# 리스트
for element in [1, 2, 3]:
    print(element) # 1 ,2, 3

# 튜플
for element in (1, 2, 3):
    print(element) # 1, 2, 3

# 셋 (집합 자료형 - 순서X, 중복X)
for element in set("hello"):
    print(element) # e, l , o , h

# 딕셔너리
for element in {1, 2, 3}:
    print(element) # 1, 2, 3

for key in {"a":1,"b":2,"c":3}: # 그냥 하면 key값만 
    print(key) # a, b, c

for key, value in {"a":1,"b":2 ,"c":3}.items(): # .items()함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍 얻을 수 있음.
    print(key, value) # a 1, b 2, c 3

# 문자열
for char in "123":
    print(char) # 1, 2, 3

# lines of file
for line in open("myfile.txt"):
    print(line)
```  

- iterator 객체 생성과 사용:
    1. 주어진 컨테이너 객체에 대해 ```iter()```메소드를 호출해서 이터레이터 객체를 구현함.
    2. 객체 내부의 요소를 하나씩 가져오기 위해서 ```__next__()```메소드를 호출함. (이 메소드는 하나의 요소를 반환하고 다음 요소르 가리킴)
    3. 더 이상 가져올게 없으면 ```StopIteration``` 예외를 발생시킴.
    - 이터레이터에 대해서 다음 요소를 직접 가져오기 위해 내장 함수인 ```next()```를 사용할 수 있음.

    ```py
    s = 'abc'
    it = iter(s)

    print(it.__next__()) # a
    print(it.__next__()) # b
    print(it.__next__()) # c
    print(it.__next__()) # StopIteration

    # 또는

    print(next(it)) # a
    print(next(it)) # b
    print(next(it)) # c
    print(next(it)) # StopIteration
    ```  

- Reverse Iterator:
```py
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self): # 문자열 자체가 iterable이므로 그냥 리턴
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration # raise - 오류 강제 발생시킬 때 사용
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for c in rev:
    print(c, end="") # 출력 결과: maps
```

# 제너레이터(Generator)

- 이터레이터(Iterator)를 만들 수 있는 **훨씬 간단**하고 **직관적인** 방법.
- 일반적인 함수처럼 작성되지만 데이터를 반한하기 위해 return 대신 ```yield``` 사용.
- 매번 next()메서드가 호출될 때마다 제너레이터는 **중단된 지점부터 다시 시작**함.(**모든 데이터 값과 마지막 실행된 명령문을 기억함**)
- 즉, return의 경우엔 값이 반환될 때마다 내부 지역변수들이 사라지지만  
  ```yield```의 경우, **내부 값들이 보존**됨.
- 리소스에 대한 제어가 필요할 때 매우 유용하게 사용됨!

- 제너레이터 사용 예시:
```py
class Reverse: # Reverse generator
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        for index in range(self.index-1, -1, -1): # 0이 될때까지 하나씩 줄여나감.
            yield self.data[index]

    rev = Reverse('spam')
    for c in rev:
        print(c, end="") # 출력결과 = maps
```
```py
# 조금 더 간단하게
def reverse(data):
    for index in range(len(data)-1, -1, -1): # 0 될때까지 하나씩 감소
        yield data[index] # 맨 뒤 인덱스 부터 인덱스 0까지 호출

for char in reverse('golf'):
    print(char, end="") # 출력결과 = flog
```  

- 제너레이터 표현식:
    - list comprehension과 유사한 문법을 사용해서 간결하게 코딩 가능!
    - 대괄호 대신 **괄호** 사용!
    - 함수의 인자로 즉시 사용되는 상황을 위해 디자인된 것.
    ```py
    sum(i*i for i in range(10)) # 0부터 9까지 제곱의 총합 => 285
    ```
    ```py
    # 출력 내용 확인
    for val in (i*i for i in range(10)):
        print(val)  # 1 4 9 16 25 36 49 64 81
    ```  
    - *list comprehension*:
        - 입력 Sequence로부터 지정된 표현식(조건)에 따라 새로운 리스트를 만듦.
        - [출력표현식 **for** 요소 **in** 입력sequence **if 조건식**]
        - 대괄호 사용
        ```py
        result = [x for x in [1,2,3,4,5] if x % 2 == 0]
        print(result) # 결과 리스트 = [2, 4] 
        ```
    