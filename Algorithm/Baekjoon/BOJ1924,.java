/* 무슨 요일인지 출력하기 */
import java.util.*;

public class BOJ1924 {

    static String[] Weekdays = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
    static int[] DayOfMonth = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();

        int tmp = 0;
        for (int i = 0; i < X; ++i) {
            tmp += DayOfMonth[i];
        }
        tmp += Y;

        String res = Weekdays[tmp % 7];

        System.out.println(res);

    }
}
