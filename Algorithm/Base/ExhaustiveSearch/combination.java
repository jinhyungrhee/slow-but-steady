/* 가장 큰 두 수의 합 구하기
* 조합 : 선택 순서가 결과에 영향을 주지 않은 경우
* 재귀호출 사용
*/
import java.util.*;

public class combination {
    static int N = 4;
    static int[] Nums = {1, 2, 3, 4};

    // pos : 현재 위치
    // cnt : 선택된 개수
    // val : 중간 계산 결과 값
    static int solve(int pos, int cnt, int val) {
        // Base case (재귀 호출 종료)
        // 2개의 수가 선택된 경우 값을 리턴함
        if (cnt == 2) return val;
        // 숫자 2개가 선택되지 않고 끝까지 간 경우 -> 경우의 수에서 제외
        if (pos == N) return -1;

        // Recursive case
        int ret = 0;
        // 해당 위치의 값을 선택
        ret = Math.max(ret, solve(pos + 1, cnt + 1, val + Nums[pos]));
        // 해당 위치의 값을 선택하지 않음
        ret = Math.max(ret, solve(pos + 1, cnt, val));

        return ret;
    }

    public static void main(String[] args) {
        System.out.println(solve(0, 0, 0));
    }

}

/*
1 - 2          : 3
  ∟ x - 3      : 4
      ∟ x - 4  : 5
          ∟ x

x - 2 - 3      : 5
  |   ∟ x - 4  : 6
  |       ∟ x
  ∟ x - 3 - 4  : 7
      |   ∟ x
      ∟ x - 4
          ∟ x
*/

/* 조합을 사용한 경우의 수 문제를 순열로 나열해도 구할 수는 있지만
*  '조합'이 경우의 수가 더 적기 때문에, 순열로 동일한 문제를 풀었을 경우 제한 시간이 초과될 수도 있음! */