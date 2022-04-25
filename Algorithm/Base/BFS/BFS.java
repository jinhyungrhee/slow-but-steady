import java.util.*;

class Main{
  // 방문 여부 
  public static boolean[] visited = new boolean[9];
  // 인접 리스트
  public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

  // BFS 함수
  public static void bfs(int start) {
    Queue<Integer> q = new LinkedList<>(); // 연결리스트-큐 자료구조 사용
    q.offer(start); // 추가
    visited[start] = true; // 방문처리
    // 큐가 빌 때까지 반복!
    while(!q.isEmpty()) {
      // 큐에서 원소 하나 뽑아서 출력
      int x = q.poll();
      System.out.print(x + " ");
      // 뽑은 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      for (int i = 0; i < graph.get(x).size(); i++) {
        int y = graph.get(x).get(i); 
        if(!visited[y]) {
            q.offer(y);
            visited[y] = true;
        }
      }
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
    graph.get(3).add(5);

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
    bfs(1); // 1 2 3 8 7 4 5 6
  }
}