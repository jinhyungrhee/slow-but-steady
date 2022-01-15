class Node {
    // 멤버 데이터
    int data;
    Node next = null;
    
    // 생성자
    Node (int d) {
        // 노드 생성시 인풋을 받아서 데이터로 할당
        this.data = d;
    }
    // 추가
    void append(int d) {
        Node end = new Node(d);
        // 포인터를 만들어 첫 번째 노드를 가리키도록 함
        Node n = this;
        while(n.next != null) {
            n = n.next;
        }
        // 마지막 노드의 next 값에 새로 생성한 노드를 넣어줌
        n.next = end;
    }
    // 삭제
    void delete(int d) {
        // 임의의 포인터 생성하여 첫 번째 노드를 가리킴
        Node n = this;
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
        // 처음부터 찾기 위한 노드 포인터 선언
        Node n = this;
        while(n.next != null){
            System.out.print(n.data+"->");
            n = n.next;
        }
        System.out.println(n.data);
    }
}

// 테스트 클래스 생성
public class SinglyLinkedList {
    public static void main(String[] args) {
        // 헤드 노드(시작 노드) 생성
        Node head = new Node(1);
        // append
        head.append(2);
        head.append(3);
        head.append(4);
        head.retrieve();
        // delete
        head.delete(2);
        head.delete(3);
        head.retrieve();

        // 한계 : 첫번째 데이터의 값은 지울 수가 없음!(헤더노드이기 때문!)
    }
}