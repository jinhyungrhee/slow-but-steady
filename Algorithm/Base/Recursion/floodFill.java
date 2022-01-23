/* Flood fill 알고리즘 
* 임의의 시작위치에서 상하좌우로 재귀호출하는 알고리즘
* Base case가 하나 이상일 수 있고, Recursive case도 하나 이상일 수 있음!
* Todo : 경계면을 만나거나 벽(1)을 만날 떄까지 모두 1로 마킹함
* 입력 : 배열의 크기 n (n x n)와 배열 그리고 시작 위치 (x, y)가 입력으로 주어짐 (0은 '빈 곳'을, 1은 '벽'을 의미함)
*/

import java.util.*;
public class floodFill {
    static int N; // 입력 받을 값을 담기 위한 변수
    static int[][] Board = new int[100][100]; // 이차원 배열 생성

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        // 이차원 배열의 원소를 입력받음
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                Board[i][j] = sc.nextInt();
            }
        }

        // 시작 위치 입력받음
        int sRow, sCol;
        sRow = sc.nextInt();
        sCol = sc.nextInt();

        // 시작 위치를 parameter로 fill 함수 호출
        fill(sRow, sCol);
        
        // 출력
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(Board[i][j] + " ");
            }
            System.out.println();
        }
    }
    // fill 함수 정의
    static void fill(int r, int c) {
        // Base case(= 재귀호출을 종료하는 부분)
        // row좌표가 경계면을 벗어나거나 col좌표가 경계면을 벗어나면, 아무것도 하지 않고 리턴
        if (r < 0 || r > N - 1 || c < 0 || c > N - 1) return;
        // 벽을 만났거나 이미 마킹된 좌표라면, 아무것도 하지 않고 리턴
        if (Board[r][c] != 0) return;

        // Recursive case
        // 빈 곳에 1을 마킹
        Board[r][c] = 1;

        fill(r - 1, c); // 위쪽으로 이동
        fill(r + 1, c); // 아래쪽으로 이동
        fill(r, c - 1); // 왼쪽으로 이동
        fill(r, c + 1); // 오른쪽으로 이동

    }
}

/* 입력
5
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
1 1 1 1 0
0 0 0 0 0
1 1
 */

/* 출력
1 1 1 1 1
1 1 1 1 1
1 1 1 1 0
1 1 1 1 0
0 0 0 0 0
 */