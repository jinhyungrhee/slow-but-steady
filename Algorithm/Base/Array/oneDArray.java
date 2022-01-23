import java.util.*;

public class oneDArray {
    static int N; // main함수 안에서 사용하기 위해 static 지정
    static int[] Score = new int[100];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 표준입출력 사용
        N = sc.nextInt(); // 정수값 입력 받아 N으로 지정
        
        // 정수 값 입력받아 배열의 원소로 저장
        for (int i = 0; i < N; i++) {
            Score[i] = sc.nextInt();
        }

        // 배열 출력
        for (int i = 0; i < N; i++) {
            System.out.print(Score[i] + " ");
        }

    }

}
