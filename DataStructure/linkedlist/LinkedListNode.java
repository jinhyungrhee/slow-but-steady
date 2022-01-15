class LinkedList {
    // 헤더(첫 번째 노드)는 데이터로 사용되지 않음
    // 관리용도로만 사용
    Node header;

    static class Node {
        int data;
        Node next = null;
    }
    
    // 생성자
    LinkedList() {
        // LinkedList를 생성할 때 header 노드 생성
        header = new Node();
    }
    // 추가
    void append(int d) {
        Node end = new Node();
        end.data = d;
        // 포인터를 만들어 헤더 노드를 가리키도록 함
        Node n = header;
        while(n.next != null) {
            n = n.next;
        }
        // 마지막 노드의 next 값에 새로 생성한 노드를 넣어줌
        n.next = end;
    }
    // 삭제
    void delete(int d) {
        // 헤더를 포인터에 할당하여 시작위치로 지정
        // 헤더는 데이터로 사용되지 않고, 관리용도로만 사용!
        Node n = header;
        // 처음부터 탐색하며 지워야할 값 찾기
        while (n.next != null) {
            // 다음 노드를 지울지 말지를 전 노드에서 판단
            if (n.next.data == d) { // "찾는 값인 경우"
                // 현재 노드의 다음을 새로 설정(다음다음 노드로)
                n.next = n.next.next;
            } else { // "찾는 값이 아닌 경우"
                // 계속 다음 노드 탐색
                n = n.next;
            }
        }
    }

    // 결과값
    void retrieve(){
        // 헤더 다음 노드를 포인터(n)에 할당 - 헤더 다음 노드부터 쭉 탐색하면서 출력
        Node n = header.next;
        while(n.next != null){
            System.out.print(n.data+"->");
            n = n.next;
        }
        System.out.println(n.data);
    }
}

// 테스트 클래스 생성
public class LinkedListNode {
    public static void main(String[] args) {
        // linked list 선언
        LinkedList ll = new LinkedList();
        // append
        ll.append(1);
        ll.append(2);
        ll.append(3);
        ll.append(4);
        ll.retrieve();
        // delete
        ll.delete(1);
        ll.retrieve();
        // 해결 : 첫번째 노드 삭제 가능
        // (첫번째 노드가 헤더노드가 아니기 때문! 헤더노드는 별도로 저장되어 관리용도로만 사용!)

    }
}
