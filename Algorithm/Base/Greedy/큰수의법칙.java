import java.util.*;

public class Main{

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // N, M, K를 공백을 기준으로 구분하여 입력 받음
    int n = sc.nextInt();
    int m = sc.nextInt();
    int k = sc.nextInt();

    // N개의 수를 공백을 기준으로 구분하여 입력 받음
    int[] arr = new int[n]; // n 크기의 배열 생성
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }

    Arrays.sort(arr); // 입력받은 수 정렬
    int first = arr[n - 1]; // 가장 큰 수
    int second = arr[n - 2]; // 두번째 큰 수

    // 가장 큰 수가 더해지는 횟수 계산
    int cnt = (m / (k + 1)) * k;
    cnt += m % (k + 1);

    int result = 0;
    result += cnt * first; // 가장 큰 수 더하기
    result += (m - cnt) * second; // 두 번째로 큰 수 더하기

    System.out.println(result);
    
  }
}