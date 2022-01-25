/* 스택을 이용한 DFS */
/*
그래프 :
    0
  ∕    ∖
  1     2
∕   ∖  ∕
3  -  4

입력:
// 노드의 수, 간선의 수
5 6
// 간선 쌍
0 1 0 2 1 3 1 4 2 4 3 4
 */
import java.util.*;

public class stackDFS {
    static final int MAX_N = 10;
    static int N, E;
    static int[][] Graph = new int[MAX_N][MAX_N];
    // stack을 사용하면 Visited 배열을 로컬 변수로 사용!
    // 재귀호출에서 Visited 배열을 global 변수로 사용하는 이유는, 함수가 호출될 때마다 배열이 스택메모리에 잡히지 않게 하기 위해!
    // -> 재귀호출이 무수히 많이 일어나도 stack overflow가 일어나지 않도록

    static void dfs(int node) {
        // 스택을 사용하면 재귀호출을 할 필요가 없기 때문에 Visited 배열을 local 변수로 선언해도 괜찮음
        boolean[] Visited = new boolean[MAX_N];
        // 스택 생성
        Stack<Integer> mystack = new Stack<>();
        // 시작 노드를 스택에 push
        mystack.push(node);

        // 빈 스택이 아닌동안 반복
        while(!mystack.empty()) {
            // 가장 최근에 push 된 인접노드가 먼저 pop되므로 DFS로 탐색됨(=우선 끝까지 내려감!)
            int curr = mystack.pop();

            // 노드에 방문한 적이 있으면 skip (=아래 코드로 이동하지 않고, 다시 while() 조건문으로 이동)
            if (Visited[curr]) continue;

            // 방문한 적이 없으면 마킹 & 출력
            Visited[curr] = true;
            System.out.print(curr + " ");
            
            // 인접 노드들 탐색
            for (int next = 0; next < N; ++next) {
                // 아직 방문하지 않았고, 인접한 노드라면
                if (!Visited[next] && Graph[curr][next] != 0) {
                    // 모두 스택에 push
                    mystack.push(next);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        E = sc.nextInt();
        for (int i = 0; i < E; ++i) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            Graph[u][v] = Graph[v][u] = 1;
        }
        dfs(0); // 0번 노드부터 DFS 탐색 시작
    }

}

/* 스택을 이용한 DFS에서는 "cyclic graph"인 경우, 스택 안의 노드가 중복될 수 있음! */
/* 출력 :
 0 2 4 3 1  */