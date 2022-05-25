import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    // n : 가게의 부품 개수
    int n = sc.nextInt();

    // set자료형 사용
    HashSet<Integer> s = new HashSet<>();
    for (int i = 0; i < n; i++) {
      int x = sc.nextInt();
      s.add(x);
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
      if (s.contains(targets[i])) {
        System.out.print("yes ");
      } else {
        System.out.print("no ");
      }
    }

    // hashSet 출력하기 (iterator 사용)
    Iterator iter = s.iterator();
    while(iter.hasNext()) {
      System.out.print(iter.next() + " "); // 2 3 7 8 9
    }
  }
}

/*
5
8 3 7 9 2 
3
5 7 9
*/