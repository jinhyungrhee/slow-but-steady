import java.util.*;

class Main{
  // 방문 여부 
  public static boolean[] visited = new boolean[9];
  // 인접 리스트
  public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

  // DFS 함수
  public static void dfs(int x) {
    // 현재 노드 방문 처리
    visited[x] = true;
    // 현재 방문 노드 출력
    System.out.print(x + " ");
    // 현재 노드와 연결된 다른 노드들 재귀적으로 방문
    for (int i = 0; i < graph.get(x).size(); i++) {
      int y = graph.get(x).get(i);
      if (!visited[y]) dfs(y);
    }
  }
  
  public static void main(String[] args) {
    // 그래프 초기화
    for (int i = 0; i < 9; i++) {
      graph.add(new ArrayList<Integer>());
    }
    // 노드 1에 연결된 노드 정보 저장
    graph.get(1).add(2);
    graph.get(1).add(3);
    graph.get(1).add(8);
    // 노드 2에 연결된 노드 정보 저장
    graph.get(2).add(1);
    graph.get(2).add(7);

    graph.get(3).add(1);
    graph.get(3).add(4);
    graph.get(3).add(7);

    graph.get(4).add(3);
    graph.get(4).add(5);

    graph.get(5).add(3);
    graph.get(5).add(4);

    graph.get(6).add(7);

    graph.get(7).add(2);
    graph.get(7).add(6);
    graph.get(7).add(8);

    graph.get(8).add(1);
    graph.get(8).add(7);

    // dfs 수행
    dfs(1); // 1 2 7 6 8 3 4 5
  }
}

