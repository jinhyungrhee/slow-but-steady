/*
클래스별 생성 방법

T는 객체 타입 : Integer, String, Double, Long 같은 Wrapper Class부터 사용자 정의 객체까지 가능!
ex) LinkedList<Integer> list = new LinkedList<>();
주의) primitive type은 불가능!
*/

// 방법1
ArrayList<T> arrayList = new ArrayList<>();
LinkedList<T> linkedList = new LinkedList<>();
Vector<T> vector = new Vector<>();
Stack<T> stack = new Stack<>();

// 방법2
List<T> arrayList = new ArrayList<>();
List<T> linkedList = new LinkedList<>();
List<T> vector = new Vector<>();
List<T> stack = new Stack<>();

// Stack은 Vector를 상속하기 때문에 아래처럼 생성 가능!
Vector<T> stack = new Stack<>();


// [자료 출처] : https://st-lab.tistory.com/142