#include <iostream>
using namespace std;

// 반복적으로 구현한 n!
int factorial_iterative(int n) 
{
	int result = 1;
	// 1부터 까지의 수를 차례대로 곱하기
	for (int i = 1; i <= n; i++) {
		result *= i;
	}
	return result;

}

// 재귀적으로 구현한 n!
int factorial_recursive(int n)
{
	if (n <= 1) {
		return 1;
	}

	// n! = n * (n - 1)!를 그대로 코드로 작성
	return n * factorial_recursive(n - 1);

}

int main() {
	cout << "반복적으로 구현 : " << factorial_iterative(5) << endl;
	cout << "재귀적으로 구현 : " << factorial_recursive(5) << endl;

	return 0;
}