import java.util.*;

class Main{

  public static int binarySearch(int[] array, int target, int start, int end) {
    while (start <= end) {
      int mid = (start + end) / 2;
      // 찾은 경우 중간점 인덱스 반환
      if (array[mid] == target) return mid;
      // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
      else if (array[mid] > target) end = mid - 1;
      // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      else start = mid + 1;
    }
    return -1;
  }

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    int[] array = new int[n];
    for (int i = 0; i < n; i++) {
      array[i] = sc.nextInt();
    }

    Arrays.sort(array);
    
    int m = sc.nextInt();

    for (int i = 0; i < m; i++) {
      int k = sc.nextInt();
      int result = binarySearch(array, k, 0, n - 1);

      if (result == -1) {
        System.out.print("no ");
      } else {
        System.out.print("yes ");
      }
      
    }
  }
}