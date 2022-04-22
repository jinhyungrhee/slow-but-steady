import java.util.*;

class Main{

  // 반복적 n!
  public static int factorialIterative(int n) {
    int result = 1;
    // 1부터 n까지의 수를 차례로 곱하기
    for (int i = 1; i <= n; i++) {
      result *= i;
    }
    return result;
  }

  // 재귀적 n!
  public static int factorialRecursive(int n) {
    // 종료 조건 (n이 1 이하인 경우 1 반환)
    if (n <= 1) return 1;
    // 재귀 부분 (n! = n * (n - 1)! 수행)
    return n * factorialRecursive(n - 1);
  }

  public static void main(String[] args) {
    System.out.println("반복적 팩토리얼 : " + factorialIterative(5));
    System.out.println("재귀적 팩토리얼 : " + factorialRecursive(5));
    
  }
}
