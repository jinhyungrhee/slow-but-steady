/* 큐를 이용한 BFS */
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
public class queueBFS {
    static final int MAX_N = 10;
    // 노드, 간선의 수
    static int N,E;
    // 인접 배열로 표현
    static int[][] Graph = new int[MAX_N][MAX_N];

    static void bfs(int node) {
        boolean[] visited = new boolean[MAX_N];
        // queue 생성
        Queue<Integer> myqueue = new LinkedList<>();
        // enqueue하기 전에 마킹함!
        // 먼저 enqueue된 것이 항상 먼저 dequeue되어 방문되기 때문 -> 나중에 동일한 노드를 enqueue하는 것은 의미가 없음!
        visited[node] = true;
        // 첫 번째 노드 enqueue
        myqueue.add(node);

        while(!myqueue.isEmpty()) {
            // dequeue ("방문했다는 의미"로 노드 번호 출력!)
            int curr = myqueue.remove();
            System.out.print(curr + " ");
            // 인접 노드 enqueue
            for (int next = 0; next < N; ++next) {
                // 방문한 적이 없고 간선이 존재한다면
                if (!visited[next] && Graph[curr][next] != 0) {
                    // 마킹 먼저 수행
                    visited[next] = true;
                    // 그 다음 enqueue
                    myqueue.add(next);
                }
            }

        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        E = sc.nextInt();

        for (int i = 0; i < E; ++i) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            // 방향성이 없는 그래프
            Graph[u][v] = Graph[v][u] = 1;
        }
        bfs(0); // 시작 노드의 위치
    }
}

/* 출력:
0 1 2 3 4 
 */
