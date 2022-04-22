import java.util.*;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // 버퍼 비우기
        sc.nextLine();
        // 이동 계획 문자들 배열에 저장 -> 공백으로 분리해도 dataType은 여전히 string!
        String[] plans = sc.nextLine().split(" ");
        int x = 1, y = 1;

        // L R U D
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        char[] moveTypes = {'L', 'R', 'U', 'D'};

        // 이동 계획 확인
        for (int i = 0; i < plans.length; i++) {
            char plan = plans[i].charAt(0); // charAt(0) : sc.nextLine().split(" ")으로 공백으로 분리해도 dataType이 string이기 때문에 charAt(0) 필요!
            // 이동 후 좌표 구하기
            int nx = -1, ny = -1; // 왜 -1? : dummy value
            for (int j = 0; j < 4; j++) {
                if (plan == moveTypes[j]) {
                    nx = x + dx[j];
                    ny = y + dy[j];
                }
            }
            // 공간을 벗어난 경우 무시
            if (nx < 1 || ny < 1 || nx > n || ny > n) continue;
            // 공간 안인 경우 이동 수행
            x = nx;
            y = ny;
        }
        System.out.println(x + " " + y);
    }
}