/* 두 수의 합이 7인 경우의 수 찾기 */
import java.util.*;

public class twoSum {
    static int N;
    static int[] Arr = new int[10];
    static int solve() {
        int ret = 0;
        // 모든 부분 집합 나열
        for (int i = 0; i < (1 << N); i++) { // (1 << N) == 2^N 개
            if (Integer.bitCount(i) != 2) // 원소의 개수가 2가 아닌 경우 skip
                continue;
            
            // 원소의 개수가 2개인 경우
            int sum = 0;
            // 부분 집합의 원소 더하기
            for (int j = 0; j < N; j++) {
                // j만큼 1을 왼쪽으로 shift하면 인덱스에 해당하는 원소만 1로 켜짐
                if ((i & 1 << j) != 0)
                    sum += Arr[j];
            }
            // 결과값이 7이면 ret값 증가시킴
            if (sum == 7) ++ret;
        }

        return ret;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            Arr[i] = sc.nextInt();
        }

        System.out.println(solve());
    }

}

/* 입력
6
1 2 3 4 5 6
*/

/* 출력
3
 */
