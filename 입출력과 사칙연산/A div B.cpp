#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	double a = 0.0, b = 0.0;
	
	cin >> a >> b;
	printf("%0.9lf", a / b); //상대오차가 소수 9자리 이하이어야 하므로 0.9lf사용

	return 0;
}
