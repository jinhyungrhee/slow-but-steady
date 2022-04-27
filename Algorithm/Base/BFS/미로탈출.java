import java.util.*;

class Node {
    // 멤버 변수
    private int x;
    private int y;
    // 생성자
    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
    // getter, setter 함수
    public int getX() {
        return this.x;
    }
    public int getY() {
        return this.y;
    }

}

public class Main {

    public static int n, m;
//    public static int[][] Board = new int[200][200];
    public static int[][] Board = new int[201][201];
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static int bfs(int x, int y) {
//        Queue<ArrayList<Integer>> q = new LinkedList<ArrayList<Integer>>();
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(x, y));
        while(!q.isEmpty()) {
            Node node = q.poll();
            x = node.getX();
            y = node.getY();
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (Board[nx][ny] == 0) continue;
                // 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if (Board[nx][ny] == 1) {
                    Board[nx][ny] = Board[x][y] + 1;
                    q.offer(new Node(nx, ny));
                }
            }
        }
        // 탈출구(가장 오른쪽 아래)까지의 최단 거리 반환
        return Board[n-1][m-1];
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            for (int j = 0; j < m; j++) {
                Board[i][j] = str.charAt(j) - '0';
            }
        }

//        for (int i = 0; i < n ; i++) {
//            for (int j = 0; j < m; j++) {
//                System.out.print(Board[i][j]+" ");
//            }
//            System.out.println();
//        }

        System.out.println(bfs(0,0));
    }
}