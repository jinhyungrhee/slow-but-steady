import java.util.*;

// 노드 클래스 생성
class Node {
  // 멤버 변수
  private int index;
  private int distance;
  // 생성자
  public Node(int index, int distance) {
    this.index = index;
    this.distance = distance;
  }
  // 멤버함수
  public void show() {
    System.out.print("(" + this.index + "," + this.distance + ") ");
  }
}


class Main{
  // Node를 원소로 갖는 이차원 ArrayList(가변길이 선형리스트) 생성
  public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
  
  public static void main(String[] args) {
    // 그래프 초기화 (= 행(row)이 3개인 인접 리스트 표현)
    for (int i = 0; i < 3; i++) {
      graph.add(new ArrayList<Node>());
    }

    System.out.println(graph); // [[], [], []]

    // 노드 0에 연결된 노드 정보 저장 (노드, 거리)
    graph.get(0).add(new Node(1, 7));
    graph.get(0).add(new Node(2, 5));

    // 노드 1에 연결된 노드 정보 저장 (노드, 거리)
    graph.get(1).add(new Node(0, 7));

    // 노드 2에 연결된 노드 정보 저장 (노드, 거리)
    graph.get(2).add(new Node(0, 5));

    // 그래프 출력
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < graph.get(i).size(); j++) {
        graph.get(i).get(j).show();
      }
      System.out.println();
    }

    System.out.println(graph); // [[Node@3b07d329, Node@41629346], [Node@404b9385], [Node@6d311334]]
    
  }
}
