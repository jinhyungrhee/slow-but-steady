# 재귀함수(Recursion)

- 함수 내에서 (직접/간접적으로) 같은 함수를 호출하는 것

    - ex1 : sum(n) = 1 + ... + n = (1 + ... + n-1) + n = sum(n-1) + n  

    ```py
    def sum(n):
        if n == 1 : return 1
        else return n + sum(n-1) # sum()을 재귀적으로 호출!
    ```  
    ```
    호출과정:
    sum(3) = 3 + sum(2)
           = 3 + (2 + sum(1))
           = 3 + (2 + (1))
           = 3 + 3
           = 6
    ```  

    - ex2: factorial(n) = n X (n-1) X .... X 1 = n X factorial(n-1) 

    ```py
    def factorial(n):
        if n == 1: return n
        else: return n * factorial(n-1) # factorial()을 재귀적으로 호출!
    ```  
    ```
    호출과정:
    factorial(3) = 3 * factorial(2)
                 = 3 * (2 * factorial(1))
                 = 3 * (2 * 1)
                 = 3 * 2
                 = 6
    ```  
    ➡ 리턴되는 값을 가지고 계속 계산을 하며 완성해야 함(recursion stack메모리 사용)

- **재귀 호출**은 현재 함수의 상태(변수 값 등)를 ```stack```이라는 특정 메모리에 저장(push)한 후 재귀 호출을 함.
    - 재귀 호출로부터 리턴되면 stack에 저장된 상태를 pop해서 원래 상태를 복원하는 식으로 이루어짐.
    - 즉, stack의 push, pop 연산이 반복적으로 이루어지는데, 경우에 따라 큰 overhaed가 발생함.
    - 이를 제한하기 위해 대부분의 언어에서 *recursion maximum depth*(=재귀 호출을 연속적으로 호출하는 깊이)에 제한을 둠.
        - Python의 경우 1000으로 제한
        - 확인
        ```py
        import sys
        print(sys.getrecursionlimit())
        ```
        - 깊이 조정
        ```py
        sys.setrecursionlimit(100000) # 10만으로 재설정함
        ```
