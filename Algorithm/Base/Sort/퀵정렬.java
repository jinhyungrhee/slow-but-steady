import java.util.*;

class Main{

  public static void quickSort(int[] arr, int start, int end) {
    if (start >= end) return; // 원소가 1개인 경우 종료
    int pivot = start; // 피벗은 첫 번째 원소
    int left = start + 1; 
    int right = end;

    while(left <= right) {
      // 피벗보다 큰 데이터를 찾을 때까지 반복 -> arr[left]
      while (left <= end && arr[left] <= arr[pivot]) left++;
      // 피벗보다 작은 데이터를 찾을 때까지 반복 -> arr[right]
      while (right > start && arr[right] >= arr[pivot]) right--;
      // 엇갈렸다면 작은 데이터(right)와 피벗 교체
      if (left > right) {
        int temp = arr[pivot];
        arr[pivot] = arr[right];
        arr[right] = temp;
      }
      // 엇갈리지 않았다면, 작은데이터(right)와 큰 데이터(left)를 교체
      else {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
      }
    }
    // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 (재귀)
    quickSort(arr, start, right - 1);
    quickSort(arr, right + 1, end);
    
  }  

  
  public static void main(String[] args) {
    int n = 10;
    int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

    quickSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++) {
      System.out.print(arr[i] + " ");
    }
    
  }
}

// Quick Sort
// 시간복잡도 : (w.c) O(n^2), (b.c) O(nlogn)