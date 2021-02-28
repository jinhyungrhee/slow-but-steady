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
    factorial(4) = 4 * factorial(3)
                 = 4 * (3 * factorial(2))
                 = 4 * (3 * 2 * factorial(1))
                 = 4 * (3 * (2 * 1))
                 = 4 * (3 * 2)
                 = 4 * 6
                 = 24
    ```  
    ➡ 리턴되는 값을 가지고 계속 계산을 하며 완성해야 함(recursion stack메모리 사용)

- **재귀 호출**은 현재 함수의 상태(변수 값 등)를 ```stack```이라는 특정 메모리에 저장(push)한 후 재귀 호출을 함.
    - 재귀 호출로부터 리턴되면 ```stack```에 저장된 상태를 pop해서 원래 상태를 복원하는 식으로 이루어짐.
    - 즉, ```stack```의 push, pop 연산이 반복적으로 이루어지는데, 경우에 따라 큰 overhaed가 발생함.
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

- Tail Recursion(Python)  

    - ex:  

    ```py
    def factorial(n, value=1):
        if n == 1: return value
        else: return factorial(n-1, value*n)
    ```  
    ```
    호출과정:
    factorial(4)
    = factorial(3, 1*4)  # value = 1
    = factorial(2, 4*3)  # value = 4
    = factorial(1, 12*2) # value = 12
    = factorial(1)       # value = 24, return value 
    ```  

    ➡TRO(Tail Recursion Optimization):  
    - 재귀함수의 매개변수로 중간 계산된 factorial값을 직접 전달함.
    - 바닥인 ```n = 1```에 도달했을 때, 이미 최종 값 24가 계산되었고 그 값을 return하여 전달만 함. 
    - ```Tail Recursion```*을 이용하면 하나의 recursion stack의 내용을 overwrite하는 식으로 메모리 사용을 크게 줄일 수 있음!*


