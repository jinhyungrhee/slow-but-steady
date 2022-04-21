import java.util.*;

class Main{
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int m = sc.nextInt();

    int result = 0;

    for (int i = 0; i < n; i++) {
      // 현재 행에서 가장 작은 수 찾기
      int min_val = 10001;
      for (int j = 0; j < m; j++) {
        int x = sc.nextInt();
        min_val = Math.min(min_val, x);
      }
      // 각 행에서 뽑은 가장 작은 수 중 가장 큰 수 찾기
      result = Math.max(result, min_val);
    }

    System.out.println(result);
  }
}