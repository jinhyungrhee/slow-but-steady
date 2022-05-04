import java.util.*;

class Main{

  public static final int MAX_VALUE = 9; // 0~9까지의 숫자 범위 (10개)
  
  public static void main(String[] args) {
    int n = 15;
    // 모든 원소의 값이 0보다 크거나 같다고 가정
    int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
    // 모든 범위를 포함하는 배열 선언(모든 값은 0으로 초기화)
    int[] cnt = new int[MAX_VALUE + 1]; // 10개의 원소를 갖는 배열 선언 및 초기화
    for (int i = 0; i < n; i++) {
      cnt[arr[i]] += 1; // 각 데이터에 해당하는 인덱스의 값 증가
    }

    for (int i = 0; i <= MAX_VALUE; i++) { // 배열에 기록된 정렬 정보 확인
      for (int j = 0; j < cnt[i]; j++) {
        System.out.print(i+ " "); // 띄어쓰기를 기준으로 등장한 횟수만큼 인덱스 출력
      } 
    }
  }
}
// 출력 결과 : 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 

// Count Sort
// 시간복잡도 : O(N + K) (N:데이터의 개수, K:데이터 중 최대값의 크기)