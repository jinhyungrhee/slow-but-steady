/*
클래스별 생성 방법

T는 객체 타입 : Integer, String, Double, Long 같은 Wrapper Class부터 사용자 정의 객체까지 가능!
단, primitive type은 불가능!
*/

ArrayDeque<T> arraydeque = new ArrayDeque<>();
PriorityQueue<T> priorityQueue = new PriorityQueue<>();

Deque<T> arraydeque = new ArrayDeque<>();
Deque<T> linkedlistdeque = new LinkedList<>();

Queue<T> arraydeque = new ArrayDeque<>();
Queue<T> linkedlistdeque = new LinkedList<>(); // 일반적인 큐
Queue<T> priorityQueue = new PriorityQueue<>();

// [자료 출처] : https://st-lab.tistory.com/142