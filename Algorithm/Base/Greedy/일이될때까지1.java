import java.util.*;

class Main{
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int k = sc.nextInt();
    int cnt = 0;

    while (n >= k) {
      // 1빼기 연산
      if (n % k != 0) {
        n -= 1;
        cnt++;
      }
      // 나누기 연산
      n /= k;
      cnt++;
    }

    // 마지막으로 남은 수에 대해 1씩 빼기
    while (n > 1) {
      n -= 1;
      cnt++;
    }

    System.out.println(cnt);

  }
}


// import java.util.*;

// class Main{
//   public static void main(String args[]) {
//     Scanner sc = new Scanner(System.in);

//     int n = sc.nextInt();
//     int k = sc.nextInt();
//     int cnt = 0;
    
//     while (n != 1) {
      
//       if (n % k != 0) {
//         n -= 1;
//         cnt++;
//       } else {
//         n /= k;
//         cnt++;
//       }
//     }

//     System.out.println(cnt);

//   }
// }