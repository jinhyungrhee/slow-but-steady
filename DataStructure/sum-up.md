## 순차적 자료구조

* 배열
* 연결리스트
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
    


