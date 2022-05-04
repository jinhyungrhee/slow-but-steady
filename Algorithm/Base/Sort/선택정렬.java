import java.util.*;

class Main{
  
  public static void main(String[] args) {

    int n = 10;
    int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

    for (int i = 0; i < n; i++) {
      int min_idx = i; // 가장 작은 원소의 인덱스
      for(int j = i + 1; j < n; j++) {
        if (arr[min_idx] > arr[j]) {
          min_idx = j;
        }
      }
      // 스와프
      int temp = arr[i];
      arr[i] = arr[min_idx];
      arr[min_idx] = temp;
    }

    for (int i = 0; i < n; i++) {
      System.out.println(arr[i] + " ");
    }
  }
}

// Selection Sort 
// 시간복잡도 : O(n^2)