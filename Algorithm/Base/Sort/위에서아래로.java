import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    // 배열 생성
    Integer[] arr = new Integer[n];
    
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }

    // 기본 정렬 라이브러리 사용한 내림차순 정렬
    Arrays.sort(arr, Collections.reverseOrder());

    for (int i = 0; i < n; i++) {
      System.out.print(arr[i] + " ");
    }
  }
}