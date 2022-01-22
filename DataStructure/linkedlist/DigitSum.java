/* 어떤 숫자를 자리수 별로 한개씩 Linked List에 담았다. 그런데 1의 자리가 헤더에 오도록 거꾸로 담았다.
* 이런식의 Linked List 두개를 받아서 합산하고 같은식으로 Linked List에 담아서 반환하라. (재귀호출 사용) */

/* 함수:(1)  (2)  (3)
*  L1 : 9 -> 1 -> 4 -> null
*  L2 : 6 -> 4 -> 3 -> null
*  C  : 0 -> 1 -> 0 -> 0 (Carry)
*  R  : 5 -> 6 -> 7      (Return 노드)
* */

class LList {
    // 헤더 노드
    Node header;

    // 노드 클래스 정의
    static class Node {
        int data;
        Node next = null;
    }
    // 생성자
    LList() {
        //링크드 리스트 생성시 header 노드 생성
        header = new Node();
    }
    // 추가 함수
    void append(int d) {
        Node end = new Node();
        end.data = d;
        // 헤더 노드를 가리키는 포인터
        Node n = header;
        while(n.next != null) {
            n = n.next;
        }
        // 마지막 노드의 next 값에 새로 생성한 노드 넣어줌
        n.next = end;
    }
    // 삭제 함수
    void delete(int d) {
        // 헤더 노드를 가리키는 포인터
        Node n = header;
        while(n.next != null) {
            if(n.next.data == d) {
                // 다음 노드가 '찾는 값'인 경우, 현재 노드의 다음을 '다음 다음 노드'로 설정
                n.next = n.next.next;
            } else {
                // '찾는 값'이 아니면, 다음 노드로 넘어감
                n = n.next;
            }
        }
    }
    // 결과 함수
    void retrieve() {
        Node n = header.next;
        while(n.next != null) {
            System.out.print(n.data + " -> ");
            n = n.next;
        }
        System.out.println(n.data);
    }
    // 첫번째 노드 반환 함수
    Node getFirst() {
        return header.next;
    }
    // n번째 노드 반환 함수
    Node get(int d) {
        Node n = header;
        for (int i = 0; i < d; i++) {
            n = n.next;
        }
        return n;
    }
}

// 테스트 클래스
public class DigitSum {
    public static void main(String[] args) {
        LList l1 = new LList();
        //l1.append(9);
        //l1.append(1);
        //l1.append(4); // 419
        l1.append(1);
        l1.retrieve();

        LList l2 = new LList();
        //l2.append(6);
        //l2.append(4);
        //l2.append(3); // 346
        l2.append(9);
        l2.append(9);
        l2.retrieve();

        // 함수 호출
        Node n = sumLists(l1.get(1), l2.get(1), 0);
        // 결과 출력
        while (n.next != null) {
            System.out.print(n.data + " -> ");
            n = n.next;
        }
        System.out.println(n.data);
    }

    // 함수 정의
    private static Node sumLists(LList.Node l1, LList.Node l2, int carry) {
        if(l1 == null && l2 == null && carry == 0) { // 바닥 조건
            return null;
        }
        // 결과를 저장할 새로운 노드 result 생성
        Node result = new Node(0);
        int value = carry;

        if (l1 != null) {
            value += l1.data;
        }
        if (l2 != null) {
            value += l2.data;
        }
        result.data = value % 10; // 몫은 carry 됨

        // 다음 노드의 값과 carry를 가지고 함수를 다시 한 번 호출함
        // 다음 함수를 호출하려면 노드가 최소한 두 개중에 하나는 null이 아니어야 함
        if (l1 != null || l2 != null) {
            // 반환 받은 값을 저장하는 공간(=노드) 생성
            Node next = sumLists(l1 == null? null : l1.next, // null 체크 한 번 더 수행
                                 l2 == null? null : l2.next, // null 체크 한 번 더 수행
                                 value >= 10? 1 : 0); // value가 10보댜 크면 carry 발생
            // 결과값을 받아와서 연결해줌
            result.next = next;
        }
        // 자기 자신을 반환
        return result;
    }
}