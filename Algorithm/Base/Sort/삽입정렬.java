import java.util.*;

class Main{
  
  public static void main(String[] args) {

    int n = 10;
    int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

    for (int i = 0; i < n; i++) {
      // 인덱스 i부터 1까지 감소하며 반복
      for (int j = i; j > 0; j--) {
        // 한 칸씩 왼쪽으로 이동하며, 
        // 선행원소(j-1)가 후행원소(j)보다 크면 swap
        if (arr[j] < arr[j - 1]) {
          int temp = arr[j];
          arr[j] = arr[j - 1];
          arr[j - 1] = temp;
        }
        // 선행원소(j-1)가 후행원소(j)보다 작으면 stop -> 적절한 위치에 삽입됨!
        else break;
      }
    }

    for(int i = 0; i < n; i++) {
      System.out.print(arr[i] + " ");
    }
  }
}

// Insertion Sort
// 시간복잡도 : (w.c) O(n^2), (b.c) O(n)