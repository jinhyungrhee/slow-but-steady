/* 최단 거리와 함께 경로 구하기 */
import java.util.*;

public class distWithPath {
    static final int INF = 987654321;
    static final int MAX_N = 10;
    static int N,E;
    static int[][] Graph = new int[MAX_N][MAX_N];
    static int[] Dist = new int[MAX_N];
    // 이전 노드를 저장하기 위한 배열
    static int[] Prev = new int[MAX_N];

    static void dijkstra(int src) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b)->a[0] - b[0]);
        boolean[] visited = new boolean[MAX_N]; // 초기값 False로 생성됨
        for (int i = 0; i < N; ++i) {
            Prev[i] = -1;
            Dist[i] = INF; // 전부 INF로 초기화
        }
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
                    Prev[v] = u;
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