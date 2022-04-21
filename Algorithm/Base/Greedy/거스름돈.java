public class Main{

  public static void main(String[] args) {
    int n = 1260;
    int cnt = 0;

    // 큰 단위의 화폐부터 차례대로 계산
    int[] coinTypes = {500, 100, 50, 10};

    for (int i = 0; i < 4; i++) {
      int coin = coinTypes[i];
      cnt += n / coin; // 해당 화폐로 거슬러 줄 수 있는 동전 개수 세기
      n %= coin;
    }

    System.out.println(cnt);
  }
  
}