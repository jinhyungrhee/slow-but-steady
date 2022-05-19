import java.util.*;

class Main{
  
  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int k = sc.nextInt();

    Integer arr1[] = new Integer[n];
    Integer arr2[] = new Integer[n];

    for (int i = 0; i < n; i++) {
      arr1[i] = sc.nextInt();
    }

    for (int i = 0; i < n; i++) {
      arr2[i] = sc.nextInt();
    }

    Arrays.sort(arr1);
    Arrays.sort(arr2, Collections.reverseOrder());

    for (int i = 0; i < k; i++) {
      if (arr1[i] < arr2[i]) {
        int temp = arr1[i];
        arr1[i] = arr2[i];
        arr2[i] = temp;
      } else break;
    }

    long sum = 0;
    for (int i = 0; i < n; i++) {
      sum += arr1[i];
    }

    System.out.println(sum);
    }
}