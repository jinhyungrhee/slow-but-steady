import java.util.*;

class Main{
  // (1)몫 나머지 연산을 통해 형변환 없이 확인하는 방법(십의자리, 일의자리)
  public static boolean check(int h, int m, int s) {
    if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3)
      return true;
    return false;
  } 
  
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int cnt = 0;

    for (int h = 0; h <= n; h++) {
      for (int m = 0; m < 60; m++) {
        for (int s = 0; s < 60; s++) {
          if (check(h, m, s)) {
            cnt++;
          } 
        }
      }
    }
    System.out.println(cnt);

    // (2)매번 String으로 바꿔서 contains()로 확인하는 방법
    
    // for (int h = 0; h <= n; h++) {
    //   for (int m = 0; m < 60; m++) {
    //     for (int s = 0; s < 60; s++) {
    //       String sH = Integer.toString(h);
    //       String sM = Integer.toString(m);
    //       String sS = Integer.toString(s);
    //       if (sH.contains("3") || sM.contains("3") || sS.contains("3")) {
    //         cnt++;
    //       } 
    //     }
    //   }
    // }
    // System.out.println(cnt);
    }
}