import java.util.*;

class Main{
  // 전역 변수로 선언
  public static int n, m, x, y, dir;
  // 북 동 남 서 
  public static int[] dx = {-1, 0, 1, 0};
  public static int[] dy = {0, 1, 0, -1};

  // 방문 위치 저장하기 위한 맵(0으로 초기화)
  public static int[][] visited = new int[50][50];
  // 전체 맵 정보
  public static int[][] map = new int[50][50];

  public static void turnLeft() {
    dir -= 1; // 왼쪽으로 회전
    if (dir == -1) dir = 3;
  }
  
  public static void main(String args[]) {
    
    Scanner sc = new Scanner(System.in);

    n = sc.nextInt();
    m = sc.nextInt();
    // x, y, dir = sc.nextLine().split(" ");
    x = sc.nextInt();
    y = sc.nextInt();
    dir = sc.nextInt();
    // 현재 좌표 방문처리
    visited[x][y] = 1;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        map[i][j] = sc.nextInt();
      }
    }

    int cnt = 1; // 방문 횟수
    int turnTime = 0; // 회전 횟수
    // 시뮬레이션
    while (true) {
      // (1) 현재 위치, 현재 방향에서 왼쪽 회전
      turnLeft();
      int nx = x + dx[dir];
      int ny = x + dy[dir];
      // (2) 가보지 않았다면(+육지라면) 전진, 가봤다면(+ 바다라면) 왼쪽으로 한 번 더 회전
      if (visited[nx][ny] == 0 && map[nx][ny] == 0) {
        visited[nx][ny] = 1;
        x = nx;
        y = ny;
        cnt += 1;
        turnTime = 0; // 전진했으므로 회전 횟수는 초기화
        continue;
      } 
      else turnTime += 1; // 어차피 다시 위로 올라가므로 회전 횟수만 추가해주면 됨
      // (3) 네 방향 모두 확인했지만, 어느 곳도 갈 수 없는 경우
      if (turnTime == 4) {
        nx = x - dx[dir];
        ny = y - dy[dir];
        // 뒤로 이동할 수 있으면 이동
        if (map[nx][ny] == 0) {
          x = nx;
          y = ny;
        }
        // 뒤가 바다라서 이동할 수 없으면 움직임 종료
        else break;
        turnTime = 0;
      }
      
    }
    System.out.println(cnt);
    
  }
}