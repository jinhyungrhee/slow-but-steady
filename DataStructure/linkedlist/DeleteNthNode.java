/* 단방향 LinkedList : 앞 노드의 정보가 없는 중간노드 삭제하기 */
class LL {
    // 헤더 노드
    Node header;
    
    // 노드 클래스 정의
    static class Node {
        int data;
        Node next = null;
    }
    // 생성자
    LL() {
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
            System.out.print(n.data + "->");
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

// test 클래스
public class DeleteNthNode {
    public static void main (String[] args) {
        LL ll = new LL();
        ll.append(1);
        ll.append(2);
        ll.append(3);
        ll.append(4);
        ll.retrieve();

        deleteNode(ll.get(3));
        ll.retrieve();
    }
    // deletNode 함수 선언
    private static boolean deleteNode(LL.Node n) {
        if (n == null || n.next == null) {
            // 노드가 null이거나 마지막 노드이면 나감!
            // 한계) 처음과 마지막 노드는 지울 수 없음!
            return false;
        }
        // '현재 노드의 다음 노드'를 받아올 Node 객체를 선언
        LL.Node next = n.next;
        // 다음 노드의 데이터와 다음 노드의 next 주소를 현재 노드에 복사함
        n.data = next.data;
        n.next = next.next;
        return true;
    }
}