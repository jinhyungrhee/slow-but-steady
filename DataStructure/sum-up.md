## 순차적 자료구조

* 배열(py-리스트) : index로 임의의 원소를 접근

* Stack, Queue, Dequeue : 제한된 접근(삽입, 삭제)만 허용
    - Stack : LIFO (Last In First Out)
    - Queue : FIFO (First In First Out)
    - Dequeue : Stack + Queue

* 연결리스트 : 연속되지 않은 메모리공간에 독립적으로 저장. 인덱스 접근 X

    - 한방향 연결리스트(Singly Linked List)
    - 양방향 연결리스트(Doubly Linked List)
        - 원형 양방향 연결리스트(Circularly Doubly Linked List)

***

## 해시 테이블(Hash table)

* 해시 함수(Hash function)
* 충돌회피방법(Collision resolution method)
    - Open addressing
        - Linear probing
        - Quadratic probing
        - double hashing
    
    - Chaining

    > Open adressing과 Chaining 모두  
      1) C-universal hash function을 사용하고  
      2) 충분한 빈 슬롯을 유지하면  
      O(1) 시간 내에 set, remove, search 함수를 수행할 수 있다!

***

## 트리구조

* 이진트리(Binary tree)
    : 자식노드가 없거나 하나거나 두개인 트리. 가장 간단하면서도 많이 쓰임.
    
    - 표현법1:  
    A = [a, b, c, None, d, e, f]

    - 표현법2:  
    A = [a, [a의 왼쪽 sub tree], [a의 오른쪽 sub tree]]  
      = [a, [b, [], [d, [], []]], [c, [e, [], []], [f, [], []]] 

    - 표현법3:  
    노드 class 직접 정의(key, left, right, parent... 최소 4개의 멤버로 정의)

    - 이진트리 순회(traversal)  
    : 이진트리 노드의 key값을 빠짐없이 출력하는 방법
        - preorder : MLR
        - inorder : LMR
        - postorder : LRM

* 힙(Heap)
    - 힙 정의: '힙 성질(Heap property)'과 '모양성질'을 만족하는 이진트리
        - 힙 성질: 모든 부모노드의 key값은 자식노드의 key값보다 작지 않다.(크거나 같아야 한다.) => max_heap
        - 모양 성질: level별로 노드가 전부 꽉 차있고 마지막 level만 왼쪽부터 채워져 있는 상태
    
    - 제공 연산:
        - insert : O(logN)
        - find_max : O(1)
        - delete_max : O(1)
        - make_heap : O(n) or O(nlogN) => insert를 n번 하는 경우
        - heapify_down : O(h) = O(logN)
        - heapify_up : O(h) = O(logN)
        - heap_sort : O(nlogN)  
        

    > 특정 값을 insert하고 가장 큰 값을 찾거나 가장 큰 값을 지우는 연산이 필요한 어플리케이션에 적절.  
      search함수가 필요한 어플리케이션에는 부적절.
    
* 이진탐색트리(Binary Search Tree, BST)  
    : search를 더 효율적으로 할 수 있도록 잘 조직화된 tree
    - 각 노드의 **왼쪽 sub tree의 key값**은 노드의 key값보다 작거나 같아야 하고
    - 각 노드의 **오른쪽 sub tree의 key값**은 노드의 key값보다 커야 한다.
      
    - 이진탐색트리의 연산
        -insert => **O(h)**  
        -search(=find_loc) => **O(h)**  
        -deleteByMerging => **O(h)**  
        -deleteByCopying => **O(h)**  

* 균형이진탐색트리(Balanced BST)  
    : 가능한 한 높이(h)를 작게 유지하도록 강제하는 바이너리 트리. 일반 BST에서는 높이가 커질수록 연산속도가 비례해서 커지기 때문!
    
    - 종류:
        - AVL트리 : 모든 노드에 대해서 노드의 왼쪽 sub tree와 오른쪽 sub tree의 높이 차이가 1 이하인 BST  

        - Red-Black트리 : 가장 유명하고 많이 사용되는 균형이진탐색트리. 5가지 조건을 따름  
            - _조건1 : 모든 노드는 red 또는 black의 색을 갖는다_  
            - _조건2 : 루트 노드는 반드시 black 노드여야 한다_  
            - _조건3 : leaf 노드(NIL)도 반드시 black 노드여야 한다_  
            - _조건4 : red 노드의 자식은 모두 black 노드여야 한다_  
            - _조건5 : 각 노드에서 leaf 노드에 이르기까지 어디로 가든 black 노드의 개수는 항상 같아야 한다_  

        - 2-3-4트리 : 자식 노드의 개수가 2개 또는 3개 또는 4개인 탐색트리. 모든 leaf노드들은 같은 level에 존재해야 한다.  

        - splay트리  

***

## 그래프 자료구조

* 두 노드 사이의 관계가 있는 경우 에지로 연결하여 표현하는 추상적이고 일반적인 자료구조  

* 그래프 G = (V, E)
    - V = 노드(node) 또는 정점(vertex) 집합
    - E = 두 노드 쌍으로 정의. (u,v)∈E 라면 노드 u와 v가 서로 (방향이 없는)에지로 연결된 것  

* 기본용어:
    - 정점(vertex), 노드(node)
    - 에지(edge), 링크(link) -> directed/undirected edge
    - 무방향 그래프, 방향 그래프
    - 분지수(degree) -> in-degree, out-degree, degree of vertex, degree of graph
    - 인접성:
        - 에지(u,v)가 존재하면, 노드 u와 노드 v는 서로 인접(adjacent)하다.
        - 에지 e =(u,v)에 대해, 에지 e는 노드 u 또는 노드 v에 인접(incident)하다.
    - 경로(path):
        - 단순 경로(simple path)
        - 경로의 길이(에지에 가중치 값이 있는/없는 경우)
    - 사이클(cycle):
        - 트리(tree): 사이클이 없는 연결 그래프
        - 포리스트(forest): 연결 트리의 콜렉션(집합)  

* 그래프 표현 방법
    - 인접행렬(adjacency matrix): 인접성을 **행렬**(2차원 배열,리스트)로 표현
        - 장점:  
                에지의 검색, 삽입, 삭제 연산을 상수 시간 내에 수행할 수 있다.
        - 단점:  
                1) 메모리를 많이 차지한다. => O(n^2)  
                2)'u에 인접한 모든 노드 v'에 대해 살펴볼 때, 인접한 노드가 존재하지 않더라도 일단 모든 노드를 체크해야 한다.
    - 인접리스트(adjacency list): 각 정점에 인접한 에지만을 **연결리스트**로 표현
        - 장점:  
                1)메모리를 적게 차지한다. => O(n+m) # n = 노드 개수 , m = 에지 개수  
                2)'u에 인접한 모든 노드 v'에 대해 살펴볼 때, 인접한 노드의 수만큼만 정확하게 for문을 돌면서 체크한다.
        - 단점:  
                에지의 검색, 삽입, 삭제 연산을 할 때 O(n)시간이 걸린다.  
                **but** '인접리스트'에서는 인접한 다른 노드들의 순서가 중요하지 않기 때문에 새 노드(에지)를 삽입 시 정렬을 할 필요가 없다. 따라서 에지 삽입 연산을 할 때 'python 리스트'를 사용하고 pushFront 대신 'append'를 사용하면 더 빠르게 연산이 가능하다. 

* 그래프 순회(Graph Traversal)
    1. DFS(깊이우선탐색, Depth First Search):
        - 가장 깊은 곳까지 내려가서 올라갔다 내려갔다를 반복하는 탐색 방법
        - 구현 : (pre_time, post_time, parent 리스트 사용)
            1. 재귀적방법 
            2. 비재귀적방법 => stack 자료구조 사용  
        - **DFS를 해서 post_time이 가장 큰 순서대로 나열하면 *DAG*의 topological sorting(위상정렬) 중 하나가 됨**  
            *DAG(Directed Acyclic Graph) : 사이클이 없는 방향 그래프*
    
    2. BFS(너비우선탐색, Breadth First Search):
        - 루트노드->루트노드의 이웃노드들->이웃노드들의 이웃노드들->... 순서로 'level-by-level'로 방문하는 방법
        - queue 자료구조를 사용하고 비재귀 코드로 작성하는 것이 일반적

    3. 최단경로 문제
        - Bellman-Ford Algorithm:  
            ```py
            for i in range(n-1): # n-1 round
                for each edge(u,v) in G:
                    if dist[v] > dist[u] + w(u,v):
                        dist[v] = dist[u] + w(u,v) # relax(u,v)
            ```  
            - 수행시간: (n-1) X E = O(nE) = O(n^3) *# E는 에지의 개수. 에지의 개수는 최대 n^2까지 가능*  
        - Dijkstra Alogrithm