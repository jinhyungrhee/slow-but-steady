# 구현(Implementation)

- 완전탐색
  - 모든 경우의 수를 빠짐없이 다 계산하는 해결 방법
  - 반복문, 재귀함수를 적절히 사용하며 예외 케이스를 모두 확인해야 하는 경우가 많음
    - 일반적으로 DFS/BFS 알고리즘을 이용하여 문제 해결

- 시뮬레이션
  - 문제에서 제시하는 논리나 동작 과정을 그대로 코드로 옮겨야 하는 유형

- `itertools` 표준 라이브러리
  - 원소를 나열하는 모든 경우의 수를 고려해야 하는 경우 **순열**이나 **조합** 라이브러리 사용