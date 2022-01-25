/* DFS활용 - Flood fill
입력 :
5 // 공간의 크기(n * n)
0 0 0 0 0
0 0 0 1 1
0 0 0 1 0
1 1 1 1 0
0 0 0 0 0 // 원소 값 (0: 빈 공간, 1: 벽)
1 1 3 // 시작 위치 값(1, 1), 컬러 값(3)
*/

import java.util.*;

public class floodFill {
    static final int MAX_N = 10;
    // 상,하,좌,우 이동을 위한 Delta array
    // 첫 번째 index : 상,하,좌,우 4개의 index 사용
    // {-1, 0} : 위로 올라감, {1, 0} : 아래로 내려감, {0, -1} : 왼쪽으로 이동, {0, 1} : 오른쪽으로 이동
    // 두 번째 index : 행,열 2 개의 index 사용
    // 0 : 행, 1 : 열
    static int[][] D = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    static int N;
    static int[][] Board = new int[MAX_N][MAX_N]; // 이차원 배열
    // 각각의 위치를 표현할 Point 클래스 정의
    static class Point {
        // 데이터 멤버
        int row, col;
        // 생성자
        Point(int r, int c) { row = r; col = c;}
    }
    // dfs함수 구현
    static void dfs(int r, int c, int color) {
        // 각 위치에 대한 방문 여부 기록하는 배열
        boolean[][] visited = new boolean[MAX_N][MAX_N];
        // DFS를 위한 스택
        Stack<Point> mystack = new Stack<>();
        // 입력받은 위치 값으로 point 객체 생성해서 스택에 push
        mystack.push(new Point(r,c));

        // 스택이 빌때까지 반복
        while(!mystack.isEmpty()) {
            // 가장 최근에 push 된 인접노드가 먼저 pop되므로 DFS로 탐색됨(=우선 끝까지 내려감!)
            Point curr = mystack.pop();
            // 이미 방문한 위치면 skip -> 아래로 내려가지 않고 빠져나와 다시 while() 조건문으로 돌아감!
            if (visited[curr.row][curr.col]) continue;

            // 아직 방문하지 않은 위치면 마킹 & Board에 색칠
            visited[curr.row][curr.col] = true;
            Board[curr.row][curr.col] = color;
            
            // 상,하,좌,우 노드 탐색 (4개의 노드)
            for (int i = 0; i < 4; ++i) {
                // '새로운 행렬 좌표(nr/nc)' 생성!
                int nr = curr.row + D[i][0], nc = curr.col + D[i][1];
                // '새로운 좌표'가 경계를 벗어나지 않는지 확인 (벗어나면 skip)
                if (nr < 0 || nr > N-1 || nc < 0 || nc > N-1) continue;
                // '새로운 좌표'가 이미 방문한 위치인지 확인 (이미 방문했다면 skip)
                if (visited[nr][nc]) continue;
                // '새로운 좌표'가 벽인지 확인 (벽이라면 skip)
                if (Board[nr][nc] == 1) continue;

                // 위 조건들에 모두 해당하지 않으면 '새로운 좌표'로 Point 객체를 만들어서 스택에 push!
                mystack.push(new Point(nr, nc));
            }

        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 공간 크기 입력
        N = sc.nextInt();
        // 원소 값 입력
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                Board[i][j] = sc.nextInt();
            }
        }
        // 시작 위치 입력
        int sRow = sc.nextInt();
        int sCol = sc.nextInt(); 
        // 컬러 값 입력
        int color = sc.nextInt();
        // dfs 호출
        dfs(sRow, sCol, color);

        // 결과 출력
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                System.out.print(Board[i][j] + " ");
            }
            System.out.println();
        }
    }
}

/*
출력:
3 3 3 3 3
3 3 3 1 1
3 3 3 1 0
1 1 1 1 0
0 0 0 0 0
 */

/* 응용 : 특정 시작점부터 도착점까지의 가는 길이 있는지 확인하기 가능!
=> curr.row와 curr.col이 도착점의 좌표와 일치한다면 true 리턴
=> while문이 끝날때까지 도착점 좌표와 일치하는 curr.row와 curr.col이 나타나지 않으면 false 리턴
*/