/* 재귀 호출을 이용한 DFS */
/*
그래프 :
    0
  ∕    ∖
  1     2
∕   ∖  ∕
3  -  4

입력:
// 노드의 수, 간선의 수
5 6
// 간선 쌍
0 1 0 2 1 3 1 4 2 4 3 4
 */
import java.util.*;

public class recursionDFS {
    static final int MAX_N = 10;
    static int N, E; // N: 노드의 개수, E: 간선의 개수
    static int[][] Graph = new int[MAX_N][MAX_N]; // '인접 행렬'로 그래프 표현
    static boolean[] Visited = new boolean[MAX_N]; // '방문 여부' 표현

    // 재귀호출을 통한 DFS 구현
    static void dfs(int node) {
        Visited[node] = true; // 방문 노드 마킹
        System.out.print(node + " "); // 방문 노드 번호 출력

        // 인접한 노드에 대해서 탐색
        for (int next = 0; next < N; ++next) {
            // 방문한 적이 없고, 간선이 존재하면 DFS 재귀 호출
            if (!Visited[next] && Graph[node][next] != 0) 
                dfs(next);
        }
    }

    public static void main(String[] args) {
        // 입력 처리
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        E = sc.nextInt();
        // 간선의 개수만큼 for문을 돌면서 한 쌍씩 읽어들임
        for (int i = 0; i < E; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            Graph[u][v] = Graph[v][u] = 1; // 1을 할당하여 인접한 노드 표시
        }
        dfs(0); // 0번 노드부터 DFS 탐색 시작
    }
}

/* 출력:
0 1 3 4 2 */