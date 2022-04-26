# Java Collections Framework

- Collection을 구현한 클래스 및 인터페이스들은 모두 `java.util` 패키지에 존재
- Collections 프레임워크는 크게 `List`, `Queue`, `Set` 인터페이스로 구성됨

## List 

- 주로 순서가 있는 데이터 목록으로 이용하도록 만들어진 인터페이스
- 이런 단점을 보완하여 List를 통해 구현된 클래스들은 '동적 크기'를 갖으면서 동시에 배열처럼 사용 가능
- **List Interface 구현 클래스**
  - `ArrayList`
    - **Object[] 배열**을 사용하면서 내부 구현을 통해 동적으로 관리
    - 요소 접근은 효율적
    - 중간 요소 삽입/삭제가 일어날 경우 그 뒤의 요소들은 한 칸씩 밀고 당겨야 하므로 비효율적
  - `LinkedList`
    - **데이터와 주소로 이루어진 클래스(=노드)**를 서로 연결하는 방식
    - 요소 검색 시 모두 방문해야 하므로 비효율적
    - 노드 삽입/삭제 시 해당 노드의 링크를 끊거나 연결만 하면 되므로 효율적
  - `Vector`(+ Vector를 상속받은 `Stack`)
    - 기본적으로 ArrayList와 유사
    - 항상 '동기화' 지원(여러 쓰레드가 동시에 데이터 접근 시 순차적 처리 보장)
    - 단일 쓰레드에서도 동기화하므로 ArrayList보다 성능 느림
- **List Interface 대표 메소드**
  |메소드|리턴 타입|설명|
  |--|--|--|
  |add(E e)|boolean|요소 추가|
  |remove(Object o)|boolean|지정한 객체와 같은 첫 번째 객체 삭제|
  |contains(Object o)|boolean|지정한 객체가 컬렉션에 있는지 확인|
  |size()|int|현재 컬렉션에 있는 요소 개수를 반환|
  |get(int index)|E|지정된 위치에 저장된 원소 반환|
  |set(int index, E elements)|E|지정된 위치에 있는 요소를 지정된 요소로 바꿈|
  |isEmpty()|boolean|현재 컬렉션에 요소가 없다면 true, 요소가 하나라도 존재한다면 false|
  |equals(Object o)|boolean|지정된 객체와 같은지 비교|
  |indexOf(Object o)|int|지정된 객체가 있는 첫 번째 요소의 위치를 반환, 없으면 -1 반환|
  |clear()|void|모든 요소들을 제거|

## Queue
- 주로 순서가 있는 데이터를 기반으로 '선입선출(FIFO)'을 위해 만든 인터페이스
- 가장 앞쪽에 있는 위치를 `head(헤드)`라고 하고, 가장 뒤(후위)에 있는 위치를 `tail(꼬리)`라고 부름
- 한쪽 방향(단방향)으로만 삽입/삭제 가능 -> tail : 삽입, head : 삭제
- Deque(Double ended Queue)
  - Queue 인터페이스를 상속하는 인터페이스
  - 양방향에서 삽입/삭제 가능 -> tail : 삽입/삭제, head : 삽입/삭제
- **Queue/Deque Interface 구현 클래스**
  - `LinkedList`
    - List를 구현하기도 하지만 Deque(=Queue)도 구현함
    - 사실상 세가지 용도로 사용 가능 : **List**, **Deque**, **Queue**
    - **Queue/Deque를 LinkedList처럼 Node 객체로 연결해서 관리하고 싶은 경우 사용!**
    - 원리 자체는 크게 다르지 않기 때문에 LinkedList 하나에 다중 인터페이스를 포함하고 있는 것
    - Java에서 '일반적인 큐'를 사용하고자 한다면 **LinkedList로 생성하여 Queue로 선언하면 됨!**
  - `ArrayDeque`
    - ArrayList처럼 Object[] 배열로 구현된 Queue/Deque을 사용할 경우
    - Deqeue는 Queue를 상속받기 때문에 Queue로도 사용 가능
  - `PriorityQueue`
    - '데이터 우선순위'에 기반하여 우선순위가 높은 데이터가 먼저 나오는 Queue (선입선출X)
    - 정렬방식을 지정하지 않으면, 낮은 숫자가 높은 우선순위를 가짐(오름차순)
    - **주어진 데이터들 중 최대값/최소값을 꺼내올 때 유용하게 사용!**
    - 주의) 사용자가 정의한 객체를 타입으로 쓸 경우, 반드시 `Comparator` 또는 `Comparable`을 통해 정렬 방식을 구현해주어야 함!
- **Queue/Deque Interface 대표 메소드**
  |분류|메소드|리턴타입|설명|
  |--|--|--|--|
  |Queue,Deque|add(E e)|boolean|요소를 꼬리에 추가, 만약 큐가 full이면 illegalStateException 예외 발생|
  |Queue,Deque|offer(E e)|boolean|요소를 꼬리에 추가, 큐가 full이더라도 illegalStateException 예외 발생X|
  |Queue,Deque|peek()|E|헤드를 삭제하지 않고 검색하여 요소 반환|
  |Queue,Deque|poll()|E|헤드를 삭제하면서 검색하여 요소 반환|
  |Deque|addLast(E e)|void|요소를 꼬리에 추가, 만약 큐가 full이면 illegalStateException 예외 발생 == `add(E e)`|
  |Deque|addFirst(E e)|void|요소를 헤드에 추가, 만약 큐가 full이면 illegalStateException 예외 발생|
  |Deque|offerLast(E e)|boolean|요소를 꼬리에 추가, 만약 큐가 full이더라도 illegalStateException 예외 발생X == `offer(E e)`|
  |Deque|offerFirst(E e)|boolean|요소를 헤드에 추가, 만약 큐가 full이면 illegalStateException 예외 발생|
  |Deque|peekFirst(E e)|E|헤드에 있는 요소를 삭제하지 않고 반환 == `peek()`|
  |Deque|peekLast(E e)|E|꼬리에 있는 요소를 삭제하지 않고 반환|
  |Deque|pollFirst(E e)|E|헤드를 검색 및 삭제하면서 요소 반환 == `poll()`|
  |Deque|pollLast(E e)|E|꼬리를 검색 및 삭제하면서 요소 반환|
  |Deque|size()|int|요소의 개수 반환|
  

  -> 왜 addLast()와 addFisrt()는 리턴타입이 void일까?
  

## Set

- 집합 자료형
  - 특징1) 데이터를 중복해서 저장할 수 없음
  - 특징2) 입력 순서대로의 저장 순서를 보장하지 않음
  -   입력받은 순서와 상관없이 데이터를 집합시키기 때문
    - 단, `LinkedHashSet`의 경우 Set임에도 불구하고 **입력 순서대로의 저장 순서 보장**
- **Set/SortedSet Interface 구현 클래스**
  - `HashSet`
    - 가장 기본적인 Set 컬렉션의 클래스 (중복 저장X, 입력 순서 보장X)
    - Hash 기능과 Set 컬렉션이 합쳐진 것으로, 삽입/삭제/색인이 매우 빠름
      - Hash : 데이터의 위치를 특정시켜 데이터를 빠르게 색인(search)할 수 있게 함!
    - 사용예시) 닉네임/아이디 중복확인
  - `LinkedHashSet`
    - 중복은 허용하지 않으면서 순서를 보장받고 싶은 경우 사용
    - 사용예시) 새로운 페이지를 할당하기 위해 최근에 사용되지 않은 cache를 비우는 경우, 가장 오래된 cache 비우기(LRU 알고리즘 -> 실제로는 LinkedHashMap 사용)
  - `TreeSet`
    - Set을 상속받은 SortedSet Interface를 구현한 것
    - 데이터의 가중치에 따른 순서대로 정렬됨
    - 중복되지 않으면서 특정 규칙에 의해 정렬된 형태의 집합을 사용하고 싶은 경우
    - 사용예시) 특정 구간의 집합 요소들을 탐색할 때 유용
- **Set/SortedSet Interface 대표 메소드**
  |분류|메소드|리턴타입|설명|
  |--|--|--|--|
  |Set,SortedSet|add(E e)|boolean|지정된 요소가 없을 경우 추가, 이미 존재하는 경우 false 리턴|
  |Set,SortedSet|contains(Object o)|boolean|지정된 요소가 Set에 있는지 확인|
  |Set,SortedSet|equals(Object o)|boolean|지정된 객체와 현재 집합이 같은지 비교|
  |Set,SortedSet|isEmpty()|boolean|현재 집합이 비어있을 경우 true, 아닐 경우 false 리턴|
  |Set,SortedSet|remove(Object o)|boolean|지정된 객체가 집합에 존재하는 경우, 해당 요소 제거|
  |Set,SortedSet|size()|int|집합에 있는 요소의 개수 반환|
  |Set,SortedSet|clear()|void|집합에 있는 모든 요소 제거|
  |SortedSet|first()|E|첫 번째 요소(가장 낮은 요소)를 반환|
  |SortedSet|last()|E|마지막 요소(가장 높은 요소)를 반환|
  |SortedSet|headSet(E toElement)|SortedSet\<E>|지정된 요소(toElement)보다 작은 요소들을 집합으로 반환|
  |SortedSet|tailSet(E fromElement)|SortedSet\<E>|지정된 요소(fromElement)를 포함하여 큰 요소들을 집합으로 반환|
  |SortedSet|subSet(E from, E to)|SortedSet\<E>|지정된 from요소를 포함하여 from보다 크고, 지정된 to 요소보다 작은 요소들을 집합으로 반환|

## Reference

- https://st-lab.tistory.com/142