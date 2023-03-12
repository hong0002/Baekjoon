/*
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
*/

#include <iostream>
using namespace std;

int main() {
	int num1 = 0, num2 = 0;
	int a = 0, b = 0, c = 0;

	cin >> num1; //첫번째 자연수
	cin >> num2; //두번째 자연수

	a = num2 % 10; //백의 자리
	b = ((num2 % 100) - a) / 10; //십의 자리
	c = (num2 - (b * 10) - a) / 100; //일의 자리

	cout << num1 * a << endl << num1 * b << endl << num1 * c << endl << num1 * num2;

	return 0;
}
