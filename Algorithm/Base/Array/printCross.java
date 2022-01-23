/* 2차원 배열 연습 - 십자가 출력
* 벽(2)을 만날때까지 상하좌우로 이동하여 십자가(1) 그리기 */
import java.util.*;

public class printCross {
    static int Row, Col;
    static int Sr, Sc; // 시작 row, 시작 col
    static int[][] Board = new int[100][100];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Row = sc.nextInt();
        Col = sc.nextInt();

        // 이차원 배열 입력 받기
        for (int i = 0; i < Row; i++) {
            for (int j = 0; j < Col; j++) {
                Board[i][j] = sc.nextInt();
            }
        }

        // 시작 위치 입력받기
        Sr = sc.nextInt();
        Sc = sc.nextInt();
        // cross 함수 호출
        cross();

        // 결과 출력
        for (int i = 0; i < Row; ++i) {
            for (int j = 0; j < Col; ++j) {
                System.out.print(Board[i][j] + " ");
            }
            System.out.println();
        }

    }

    // cross 메서드 정의
    static void cross() {
        // 시작 위치가 비어있지 않으면 십자가 긋기 불가(바로 리턴)
        if (Board[Sr][Sc] != 0) return;
        // 비어 있으면 해당 위치부터 1로 마킹
        Board[Sr][Sc] = 1;

        // 위로 올라가면서 탐색
        for (int i = Sr - 1; i >= 0; --i) {
            if(Board[i][Sc] != 0) break;
            Board[i][Sc] = 1;
        }
        // 아래로 내려가면서 탐색
        for (int i = Sr + 1; i < Row; ++i) {
            if(Board[i][Sc] != 0) break;
            Board[i][Sc] = 1;
        }
        // 왼쪽으로 가면서 탐색
        for (int j = Sc - 1; j >= 0; --j) {
            if(Board[Sr][j] != 0) break;
            Board[Sr][j] = 1;
        }
        // 오른쪽으로 가면서 탐색
        for (int j = Sc + 1; j < Col; ++j) {
            if(Board[Sr][j] != 0) break;
            Board[Sr][j] = 1;
        }

    }
}