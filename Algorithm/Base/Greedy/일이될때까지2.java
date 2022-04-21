import java.util.*;

class Main{
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int k = sc.nextInt();
    int cnt = 0;

    while(true) {
      // 나누어 떨어지는 수가 될 때까지 1씩 빼기
      int target = (n / k) * k; 
      cnt += (n - target); 
      n = target;
      // n이 k보다 작을 때(더 이상 나눌 수 없을 때) 탈출
      if (n < k)
        break;
      // k로 나누기
      cnt++;
      n /= k;
    }

    // 마지막으로 남은 수에 대해서 1씩 빼기
    cnt += (n - 1);
    System.out.println(cnt);

  }
}