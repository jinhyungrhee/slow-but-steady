import java.util.*;

class Main{
  
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    String input = sc.nextLine();
    int row = input.charAt(1) - '0'; // numeric char(ascii) to int
    int col = input.charAt(0) - 'a' + 1; // alphabet char(ascii) to int

    // 나이트 이동 범위
    // (1) 2차원 배열
    // int[][] steps = {{-2, -1}, {-1, -2}, {1, -2}, {-2, 1}, {-1, 2}, {2, -1}, {1, 2}, {2}};
    // (2) dx-dy(1차원 배열 x2)
    int dx[] = {-2, -1, -2, -1, 2, 1, 2, 1};
    int dy[] = {-1, -2, 1, 2, -1, -2, 1, 2};

    // 8가지 방향에 대해 이동 가능한지 확인
    int result = 0;
    for (int i = 0; i < 8; i++) {
      int nRow = row + dx[i];
      int nCol = col + dy[i];

      // 2차원 배열 뽑아내기는 후에 다시 시도
      // int nRow = row + steps[i][0];
      // int nCol = col + steps[i][1];

      if (nRow >= 1 && nRow <= 8 && nCol >= 1 && nCol <= 8) {
        result++;
      }
    }
    
    System.out.println(result);
    
  }
}