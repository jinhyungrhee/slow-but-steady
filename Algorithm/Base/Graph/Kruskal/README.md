# 크루스칼 알고리즘

## 신장 트리(Spanning Tree)

- 하나의 그래프가 있을 때, `모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프`
  - '모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다'는 조건은 트리의 성립조건이기도 함!
  - 즉, `그래프 내의 모든 정점을 포함하는 트리`(=사이클 X)임!

- (1)포함되지 않은 노드가 존재하거나 (2)사이클이 존재하면 신장 트리(Spanning Tree)가 아님!

## 크루스칼 알고리즘(Kruskal Algorithm)

- 대표적인 '최소 신장 트리 알고리즘'
- 최소 신장 트리 알고리즘
  - 신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘
  - 가장 적은 비용으로 모든 노드를 연결할 수 있음
- '그리디 알고리즘'으로 분류됨  
- ex) N개의 도시가 존재할 때, 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우
- 알고리즘
  - **①** 간선 데이터를 비용에 따라 오름차순으로 정렬 
  - **②** 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    - (1) 사이클이 발생하지 않는 경우(=동일한 집합에 포함되어 있지 않은 경우), 최소 신장 트리에 포함시킴 -> union 함수 호출O
    - (2) 사이클이 발생하는 경우(=이미 동일한 집합에 포함되어 있는 경우), 최소 신장 트리에 포함시키지 않음 -> union 함수 호출X
  - **③** 모든 간선에 대하여 ②번 과정을 반복
- 정리
  - 가장 거리가 짧은 간선부터 차례대로 집합에 추가하면 됨(사이클을 발생시키는 간선 제외!) => `최적의 해` 보장!(Greedy)
  - 최소 신장 트리는 일종의 트리 자료구조이므로, 최종적으로 신장 트리에 포함되는 간선의 개수는 `노드 개수 - 1`임
  - 최소 신장 트리에 포함되어 있는 간선의 비용을 모두 더하면, 그 값이 최종 비용(=최소 비용)에 해당함
- 시간복잡도
  - 간선의 개수가 E일 때, `O(ElogE)`
  - 가장 시간이 오래 소요되는 부분이 정렬(sort) 작업임 -> E개의 데이터를 정렬했을 때의 시간복잡도 : O(ElogE)

