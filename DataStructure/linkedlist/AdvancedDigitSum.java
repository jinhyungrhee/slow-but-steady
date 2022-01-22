/* (심화) 어떤 숫자를 자리수 별로 한개씩 Linked List에 담았다. (정방향)
 * 이런식의 Linked List 두개를 받아서 합산하고 같은식으로 Linked List에 담아서 반환하라. (재귀호출 사용) */

/* 부족한 자릿수는 0으로 채움
*함수:  (3)  (2)  (1)
*  L1 : 4 -> 1 -> 9 -> null
*  L2 : 0 -> 3 -> 4 -> null
*       4    5    3
* null에 도착하면 노드(R=null)와 carry(C=0) 정보를 저장하는 객체를 생성하여 반환함
* C = 0 -> 1 -> 0
* R = 4 -> 5 -> 3 -> null
*
* 만약, 마지막 호출한 함수에서 carry가 발생하면, 합산 작업을 한 번 더 수행하여 carry를 노드로 만들어서 맨 앞에 추가함!
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


// 재귀 호출시 반환받을 객체 공간을 위한 클래스를 하나 선언
class Storage {
    int carry = 0;
    Node result = null;
}


public class DigitSum2 {
    public static void main(String[] args) {
        LList l1 = new LList();
        l1.append(9);
        l1.append(1);
        l1.retrieve();

        LList l2 = new LList();
        l2.append(1);
        l2.append(1);
        l2.retrieve();

        // 함수 호출
        Node n = sumLists(l1.get(1), l2.get(1));
        // 결과 출력
        while (n.next != null) {
            System.out.print(n.data + " -> ");
            n = n.next;
        }
        System.out.println(n.data);

    }
    // 함수 정의
    private static Node sumLists(Node l1, Node l2) {
        // 전달 받은 리스트의 길이 구함
        int len1 = getListLength(l1);
        int len2 = getListLength(l2);

        // 더 짧은 리스트 앞에 0을 채우기
        if (len1 < len2) {
            l1 = LPadList(l1, len2-len1);
        } else {
            l2 = LPadList(l2, len1-len2);
        }

        // carry와 결과값을 저장하는 storage 클래스를 반환
        // 이 부분에서 계속 addList()가 호출되면서 덧셈을 수행함
        Storage storage = addList(l1, l2);
        // 노드를 끝까지 돌았을 때, 이 재귀함수를 호출한 함수는 마지막으로 한번 더 확인 필요 -> carry 체크하기
        if (storage.carry != 0) {
            // list의 길이를 넘어서 새로운 노드를 추가해야하는 carry가 있다면 (= 맨 앞 자리에서 carry가 발생하는 경우)
            // storage의 결과 앞에, 현재 carry 값으로 새로운 노드를 생성하여 붙여줌
            storage.result = insertBefore(storage.result, storage.carry);
        }
        // 만약 carry가 0이면, storage.result가 결과값이 됨
        return storage.result;
    }
    // 필요한 기능들 함수로 정의
    // 두 리스트를 더하는 함수 - Storage 객체로 반환
    private static Storage addList(Node l1, Node l2) {
        // 두 리스트 모두 맨 끝까지 간 경우
        if (l1 == null && l2 == null) {
            // carry와 결과를 저장할 공간 생성
            Storage storage = new Storage();
            return storage; // storage 객체의 주소를 반환
        }
        // 재귀 호출
        Storage storage = addList(l1.next, l2.next);
        // ** 계속 돌면서 storage 객체의 주소를 받으면, storage.result에 노드를 추가! **
        int value = storage.carry + l1.data + l2.data; // storage.carry = storage에 carry가 있는지 확인
        // 저장해야 하는 데이터 값 ( = 현재 값을 10으로 나눈 나머지)
        int data = value % 10;
        // 이 데이터를 storage.result에 노드로 생성해서 앞에 추가함
        storage.result = insertBefore(storage.result, data);
        // storage의 carry는 현재 값을 10으로 나눈 몫임
        storage.carry = value / 10;
        return storage;
    }

    // 리스트를 받아서 길이를 반환하는 함수
    private static int getListLength(Node l) {
        int total = 0;
        while(l != null) {
            total++;
            l = l.next;
        }
        return total; // 마지막 노드에 도착했을 때, total에 총 길이가 담김
    }
    // 노드 앞에 새로운 노드를 추가하는 기능 (추가할 위치, 새로 생성할 데이터)
    private static Node insertBefore(Node node, int data) {
        // 앞에 추가할 노드(before) 생성
        Node before = new Node(data);
        if (node != null ) {
            // node를 내 다음에 위치시킴 (=나를 node 앞에 추가하는 것)
            before.next = node;
        }
        return before; // 새로 생성한 노드를 반환
    }
    // linked list와 길이값을 parameter로 받아서 왼쪽을 0으로 채워주는 함수
    private static Node LPadList(Node l, int length) {
        Node head = l; // 노드를 복사
        // 길이만큼 돌면서 head에 붙여줌
        for (int i = 0; i < length; i++) {
            head = insertBefore(head, 0); // 0이라는 값으로 length만큼 head 앞에 붙임
        }
        return head;
    }
}