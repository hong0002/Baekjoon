# -*- coding: utf-8 -*-

#두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


#첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.


#첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

a, b = map(int, (input().split()))

if b > a:
    a, b = b, a

gcd = b # 최대공약수
lcm = a # 최소공배수
while True:
    if b % gcd == 0 and a % gcd == 0:
        print(gcd)
        break
    gcd -= 1

count = int(2)
while True:
    if lcm % b == 0 and lcm % a == 0:
        print(lcm)
        break
    lcm = b * count
    count += 1
