# -*- coding: utf-8 -*-

#N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.


#첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)


#첫째 줄에 구한 0의 개수를 출력한다.

num = 1
count = 0

n = int(input())
for i in range(n, 1, -1):
    num *= i

num = str(num) # 구한 팩토리얼 문자열로 변환
num = num[::-1] # 문자열 뒤집기

for i in num:
    if i == '0':
        count += 1
    else:
        print(count)
        break
