#include <iostream>
using namespace std;

void recursive_function(int i) 
{
	// 바닥조건
	if (i == 10)
		return;
	cout << i << "번째 재귀함수에서 " << i + 1 << "번째 재귀함수를 호출합니다." << endl;
	recursive_function(i + 1);
	// return된 이후에 재개되어 실행
	cout << i << "번째 재귀함수를 종료합니다." << endl;
}

int main() {
	recursive_function(1);
}