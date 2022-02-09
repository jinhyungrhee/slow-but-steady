// 음료수 얼려먹기 - DFS
#include <iostream>

using namespace std;

// 전역변수
int n, m;
int graph[1000][1000];

// DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
bool dfs(int x, int y) {
	// 범위를 벗어나면 즉시 종료
	if (x <= -1 || x >= n || y <= -1 || y >= m)
		return false;

	// 현재 노드를 아직 방문하지 않았다면
	if (graph[x][y] == 0) {
		// 해당 노드 방문 처리
		graph[x][y] = 1;
		// 상,하,좌,우 위치 재귀호출
		dfs(x - 1, y);
		dfs(x, y - 1);
		dfs(x + 1, y);
		dfs(x, y + 1);
		return true;
	}
	return false;
}

int main() {
	// 2차원 리스트의 맵 정보 입력받기
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &graph[i][j]);
		}
	}

	int result = 0;
	// 모든 노드(위치)에 대하여 음료수 채우기
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			// 현재 위치에서 dfs 수행
			if (dfs(i, j)) {
				result += 1;
			}
		}
	}

	cout << result << '\n';

	return 0;
}