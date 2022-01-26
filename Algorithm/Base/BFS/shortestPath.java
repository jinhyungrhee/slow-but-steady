/* 2차원 좌표 공간에서 BFS를 활용해서 최단 경로 구하기 */
/* 입력:
5
0 0 0 0 0
0 1 1 1 1
0 0 0 0 0
1 1 1 1 0
0 0 0 0 0 // 0 - 빈 공간, 1 - 벽
0 1 4 2   // 0 1 - 시작점, 4 2 - 도착점
 */

import java.util.*;
public class shortestPath {
    static final int MAX_N = 10;
    static int[][] D = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static int N;
    static int[][] Board = new int[MAX_N][MAX_N];
    // 각각의 칸을 Point 클래스로 표현
    static class Point {
        int row, col, dist; // 행, 열, 거리
        Point(int r, int c, int d) {
            row = r; col = c; dist = d;
        }
    }

    static int bfs(int sRow, int sCol, int dRow, int dCol) {
        boolean[][] visited = new boolean[MAX_N][MAX_N];
        Queue<Point> myqueue = new LinkedList<>();
        // 시작 노드 마킹 먼저한 뒤 enqueue
        visited[sRow][sCol] = true;
        myqueue.add(new Point(sRow, sCol, 0));

        while (!myqueue.isEmpty()) {
            // dequeue
            Point curr = myqueue.remove();
            // dequeue한 노드가 도착점인지 확인
            if (curr.row == dRow && curr.col == dCol)
                return curr.dist;

            // 도착점이 아니면
            for (int i = 0; i < 4; ++i) {
                // 새로운 좌표를 만들어냄(상, 하, 좌. 우 이동)
                int nr = curr.row + D[i][0], nc = curr.col + D[i][1];
                // 배열의 범위를 벗어난 경우 skip
                if (nr < 0 || nr > N-1 || nc < 0 || nc > N-1) continue;
                // 이미 방문한 경우 skip
                if (visited[nr][nc]) continue;
                // 벽인 경우 skip
                if (Board[nr][nc] == 1) continue;

                // skip되지 않았으면 방문 가능한 좌표
                visited[nr][nc] = true;
                // 새로운 좌표로 거리값+1하여 새로운 노드 enqueue
                myqueue.add(new Point(nr, nc, curr.dist + 1));
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                Board[i][j] = sc.nextInt();
            }
        }

        int sRow, sCol, dRow, dCol;
        sRow = sc.nextInt();
        sCol = sc.nextInt();
        dRow = sc.nextInt();
        dCol = sc.nextInt();
        // bfs()는 최단경로 길이 반환
        System.out.println(bfs(sRow, sCol, dRow, dCol));
    }
}

/* 결과:
11
 */