# 재귀함수

- 자기 자신을 호출하는 함수
- 구분
  - Base case : 간단히 결과를 반환하는 부분
  - Recursive case : 자기 자신을 호출하는 부분
- 예시 : Factorial (수학적 귀납법 정의)
  - n = 0 이면, n! = 1 -> Base case
  - n > 0 이면, n! = n * (n-1)! -> Recursive case
    ```java
    int factorial(int n)
    {
      if (n == 0) // Base case
        return 1;
      
      return n * factorial(n-1); // Recursive case
    }
    ```
  - 스택 메모리
    - 함수 호출은 스택 메모리에 생성됨
    - 실제 코드가 스택 메모리에 올라가지는 않고, 함수 실행에 필요한 변수값들과 호출한 함수로 돌아가기 위한 return address가 저장됨
    ```
      ---------------------------
      factorial(0)
        if (0 == 0)
          return 1;
      ---------------------------
      factorial(1)
        ...
        return 1 * factorial(0);
      ---------------------------
      factorial(2)
        ...
        return 2 * factorial(1);
      ----------------------------
      factorial(3)
        ...
        return 3 * factorial(2);
      ----------------------------
      void main(String[] args)
        ...
        factorial(3);
      ----------------------------
          Stack Memory
    ```