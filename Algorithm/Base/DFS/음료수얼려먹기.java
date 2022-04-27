import java.util.*;

class Main{

  static final int MAX_N = 1000;
  static int[][] Board = new int[MAX_N][MAX_N];
  static int n, m;
  
  public static boolean dfs(int x, int y) {
    if (x <= -1 || x >= n || y <= -1 || y >= m) 
      return false;
    if (Board[x][y] == 0) {
      Board[x][y] = 1;
      dfs(x - 1, y);
      dfs(x, y - 1);
      dfs(x + 1, y);
      dfs(x, y + 1);
      return true;
    }
    return false;
  }
  
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // 띄어서 입력 받는 경우
    /* 
    n = sc.nextInt();
    m = sc.nextInt();

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        Board[i][j] = sc.nextInt();
      }
    }
    */

    // 붙여서 입력 받는 경우
    n = sc.nextInt();
    m = sc.nextInt();
    sc.nextLine(); // 버퍼 비우기

    for (int i = 0; i < n; i++) {
      String str = sc.nextLine(); // 우선 한 줄의 String으로 입력받아서
      for (int j = 0; j < m; j++) {
        Board[i][j] = str.charAt(j) - '0'; // 인덱스로 각각을 Char로 쪼개서 저장
      }
    }

    int result = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (dfs(i, j)) {
          result += 1;
        }
      }
    }

    System.out.println(result);
  }
}

