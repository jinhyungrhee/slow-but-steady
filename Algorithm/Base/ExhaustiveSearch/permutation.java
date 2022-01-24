/* 가장 큰 두 자리 수 구하기
* 순열 : 순서에 따라 결과가 달라지는 경우
* 재귀호출 사용
*/
import java.util.*;

public class permutation {
    static int N = 4;
    static int[] Nums = {1, 2, 3, 4};

    // cnt : 선택된 숫자의 개수
    // used : 사용된 숫자 (bit형태로 마킹함)
    // val : 중간 계산 결과 값
    static int solve(int cnt, int used, int val) {
        // 선택된 숫자의 개수가 2이면, 재귀호출 종료(Base case)
        if (cnt == 2) return val; //지금까지의 계산 결과를 반환

        // 재귀호출 부분(Recursive case)
        int ret = 0;
        // 모든 경우 전부 확인(= 완전탐색)
        for (int i = 0; i < N; ++i) {
            // ** 마킹을 확인하여 이미 사용된 숫자인지 체크! **
            // 사용한 숫자인 경우 skip - 최초에는 사용한 숫자가 없으므로 1, 2, 3, 4 모두 시도
            if ((used & 1 << i) != 0) continue;
            // cnt + 1 : 선택된 cnt를 하나 올려줌
            // ** used | 1 << i : 해당 숫자를 선택했다는 표시로 마킹함 **
            // val * 10 + Nums[i] : 값 계산
            ret = Math.max(ret, solve(cnt + 1, used | 1 << i, val * 10 + Nums[i]));
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(solve(0, 0, 0));
    }
}

/*
    2  : 12
  ∕
1 - 3  : 13
  ∖
    4  : 14

    1  : 21
  ∕
2 - 3  : 23
  ∖
    4  : 24

    1  : 31
  ∕
3 - 2  : 32
  ∖
    4  : 34

    1  : 41
  ∕
4 - 2  : 42
  ∖
    3  : 43
* */
