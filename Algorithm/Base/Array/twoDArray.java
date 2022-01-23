import java.util.*;

public class twoDArray {
    static int Row, Col;
    static int[][] Board = new int[100][100]; // 2차원 배열 정의

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Row = sc.nextInt();
        Col = sc.nextInt();

        // 입력
        for (int i = 0; i < Row; i++) {
            for (int j = 0; j < Col; j++) {
                Board[i][j] = sc.nextInt();
            }
        }
        // 출력
        for (int i = 0; i < Row; i++) {
            for (int j = 0; j < Col; j++) {
                System.out.print(Board[i][j] + " ");
            }
            System.out.println(); // 한 Row가 끝났으면 줄바꿈
        }

    }
}
