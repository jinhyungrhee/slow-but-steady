import java.util.*;

class Main{
  
  public static void main(String[] args) {

    int n = 10;
    int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

    List<Integer> arrayList = new ArrayList<>();

    for (int i = n - 1; i >= 0; i--) {
      arrayList.add(i);
    }

    Arrays.sort(arr);
    Collections.sort(arrayList);

    for (int i = 0; i < n; i++) {
      System.out.print(arr[i] + " ");
    }
    
    System.out.println();
    
    for (int i = 0; i < n; i++) {
      System.out.print(arrayList.get(i) + " ");
    }
  }
}
