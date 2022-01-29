/* 숫자의 합 */
import java.util.Scanner;

public class BOJ11720 {

    static int N;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        String lf = sc.nextLine(); // linefeed
        String number = sc.nextLine();

       /*
       // 방법1
       String[] strArray = number.split("");
       int sum = 0;
       for (String s : strArray){
           //System.out.println(s);
           sum += Integer.parseInt(s);
       }

       System.out.println(sum);
        */


        // 방법2
        int sum = 0;
        for (int i = 0; i < N ; ++i) {
            sum += number.charAt(i) - 48;
        }

        System.out.println(sum);
    }

}
