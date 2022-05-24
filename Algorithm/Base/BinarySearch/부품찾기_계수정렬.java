import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    // n : 가게의 부품 개수
    int n = sc.nextInt();
    // 미리 가능한 모든 범위의 수를 담을 수 있는 배열 생성
    int[] array = new int[1000001];
    for (int i = 0; i < n; i++) {
      int x = sc.nextInt();
      array[x] = 1; // 입력으로 들어온 수 기록
    }

    // m : 손님이 확인 요청한 부품 개수
    int m = sc.nextInt();
    int[] targets = new int[n]; // m아닌가? (m이 n보다 클 수 없으므로 상관 없을 듯...)
    for (int i = 0; i < m; i++) {
      targets[i] = sc.nextInt();
    }

    // 손님이 확인 요청한 부품 번호를 하나씩 확인
    for (int i = 0; i < m; i++) {
      // 해당 부품이 존재하는지 확인
      if (array[targets[i]] == 1) {
        System.out.print("yes ");
      } else {
        System.out.print("no ");
      }
    }
  }
}