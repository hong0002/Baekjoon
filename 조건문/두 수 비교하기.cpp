/*
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
*/

#include <iostream>
using namespace std;

int main() {
	int a, b;

	cin >> a >> b;

	if (a > b) { //a가 클때
		cout << ">";
	}
	else if (a < b) { //b가 클때
		cout << "<";
	}
	else { //같을때
		cout << "==";
	}

	return 0;
}
