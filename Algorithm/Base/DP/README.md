# 동적 계획법(Dynamic Programming)
- 메모리 공간을 약간 더 사용하여 연산속도를 비약적으로 증가시키는 방법

## 점화식
- 인접한 항들 사이의 관계식
- 점화식을 이용해 현재의 항을 이전의 항에 대한 식으로 표현 가능
- 수학적 점화식을 프로그래밍으로 표현하려면 재귀 함수 사용
- 예1) 피보나치 함수 (only 재귀)
  ```py
  def fibo(x):
    if x == 1 or x == 2:
      return 1

    return fibo(x - 1) + fibo(x - 2)
  
  print(fibo(4))
  ```
  - 문제점 : n이 커지면 커질수록 반복해서 호출되는 경우가 많아짐 => 시간 복잡도 : O(2^N)


## DP 조건
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

- DP와 분할 정복(Divide & conquer) 차이
  - 다이나믹 프로그래밍은 문제들이 서로 영향을 미침

## 메모이제이션(Memoization) - 탑 다운 방식
- DP 구현 방법 중 하나
- 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출할 때 메모한 결과를 그대로 가져오는 것
- '캐싱(caching)'이라고도 함
- 탑 다운(Top-Down) 방식 : 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
- 예2) 피보나치 함수 (재귀 & 메모이제이션)
  ```py
  # 계산된 결과를 저장하는 메모이제이션 리스트 초기화
  d = [0] * 100

  # 재귀호출 + 메모이제이션 => 탑다운 다이나믹 프로그래밍
  def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
      return 1
    # 이미 계산된 문제라면 그대로 반환
    if d[x] != 0:
      return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따른 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

  print(fibo(99))
  ```
  - f(1)을 구한 값이 그 다음 f(2)를 푸는 데 사용되고, f(2)의 값이 f(3)를 푸는데 사용되는 방식으로 이어짐 -> 시간 복잡도 : O(N)
  - '재귀 함수'를 사용하면 함수를 다시 호출했을 때 메모리 상에 적재되므로 오버헤드 발생 -> `for 반복문`을 사용하여 오버헤드 줄이기 가능(바텀업 다이나믹 프로그래밍)
- `사전(dict) 자료형`을 이용한 메모이제이션
  - 수열처럼 연속적이지 않은 경우에 유용
  - 예) an을 계산하고자 할 때 a0 ~ an-1 모두가 아닌 일부의 작은 문제에 대한 해답만 필요한 경우

## 타뷸레이션(Tabulation) - 바텀 업 방식
- DP 구현 방법 중 하나
- 바텀 업(Bottom-Up) 방식 : 단순히 반복문을 이용하여 소스코드를 작성하는 경우, 작은 문제부터 차근차근 답을 도출
- 다이나믹 프로그래밍의 전형적인 형태
- 예3) 피보나치 함수 (단순 반복문)
  ```py
  # 앞서 계산된 결과를 저장하는 DP 테이블 초기화
  d = [0] * 100

  # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
  d[1] = 1
  d[2] = 1
  n = 99

  # 피보나치 함수를 반복문으로 구현(바텀 업 다이나믹 프로그래밍)
  for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

  print(d[n])
  ```

## TIP
- 일단 재귀 함수로 비효율적인 프로그램(탑 다운)을 작성한 뒤, 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면(= 메모이제이션을 적용할 수 있으면) 코드를 개선하는 것도 하나의 방법!
- 시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있으므로, 탑 다운 방식보다는 `바텀 업 방식`으로 구현하는 것을 권장!
  - sys 라이브러리의 'setrecursionlimit()' 함수를 통해 재귀 제한 완화도 가능함