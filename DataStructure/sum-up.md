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


