/* 모든 정점까지 거리 구하기 (Priority Queue 사용) */
/* 입력:
6 9 // 노드, 간선 개수
0 1 50
0 2 30
1 3 30
1 4 70
2 3 20
2 4 40
3 4 10
3 5 80
4 5 30 // 간선과 가중치
 */

import java.util.*;

public class distToAllNodes {
    static final int INF = 987654321;
    static final int MAX_N = 10;
    static int N,E;
    // Graph를 '인접 행렬'로 표현
    static int[][] Graph = new int[MAX_N][MAX_N];
    static int[] Dist = new int[MAX_N];

    static void dijkstra(int src) {
        // 다음 정점을 선택할 때 우선순위 큐(PriorityQueue) 사용
        // 우선순위 큐에 들어가는 타입은 int배열로 선언 -> int 쌍을 넣기 위해
        // lambda 함수 : 두 개의 값을 비교할 때 첫 번째 인덱스로 비교!
        // 첫 번째 인덱스 - dist값(= 그 정점까지 가기 위한 최단 비용)
        // 두 번째 인덱스 - 정점의 번호
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b)->a[0] - b[0]);
        boolean[] visited = new boolean[MAX_N]; // 초기값 False로 생성됨
        for (int i = 0; i < N; ++i) Dist[i] = INF; // 전부 INF로 초기화
        Dist[src] = 0; // 현재 위치만 0 할당
        pq.add(new int[] {0, src}); // 0에서 현재위치까지의 최단거리 구하기 위해 enqueue

        while(!pq.isEmpty()) {
            // 멘 위의 노드 dequeue (힙 - 가중치가 작은 것이 가장 위로 올라옴)
            int[] curr = pq.poll();
            // 1번 인덱스로 '정점의 번호' 할당
            int u = curr[1];
            // 방문 여부 체크 후, 해당 정점에 대해 방문 마킹
            if (visited[u]) continue;

            visited[u] = true;
            // 현재 정점에서 인접한 정점들 사이의 비용 계산
            for (int v = 0; v < N; ++v) {
                // '이전에 저장되어 있는 값'과 '새로 구한 값'을 비교하여 더 작은 값으로 업데이트
                if (Dist[v] > Dist[u] + Graph[u][v]) {
                    Dist[v] = Dist[u] + Graph[u][v];
                    // 해당 값으로 enqueue
                    pq.add(new int[] {Dist[v], v});
                }
            }
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        E = sc.nextInt();
        // '노드'의 개수만큼 Graph 배열 초기화
        // 대각선(=자기자신)은 0, 이외는 무한대(INF)로 초기화
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (i == j) Graph[i][j] = 0;
                else        Graph[i][j] = INF;
            }
        }
        // '간선'마다 가중치를 할당
        for (int i = 0; i < E; ++i) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int cost = sc.nextInt();
            // 방향성이 없는 그래프 (방향성이 있으면 하나의 값만 저장)
            Graph[u][v] = Graph[v][u] = cost;
        }
        // 0을 시작위치로 하여 계산한 '모든 정점까지의 최단 경로'를 Dist 배열에 저장
        dijkstra(0);
        // 출력
        for (int i = 0; i < N; i++)
            System.out.print(Dist[i] + " ");
    }
}

/* 출력:
0 50 30 50 60 90
 */