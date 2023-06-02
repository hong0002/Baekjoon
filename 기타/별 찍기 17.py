# -*- coding: utf-8 -*-

#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.


#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.


#첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

n = int(input())

for i in range(n):
    if i == 0:
        print(' '*(n-i-1), end="")
        print('*')
    elif i == (n-1):
        print('*'*((n*2)-1))
    else:
        print(' '*(n-i-1), end="")
        print('*', end="")
        print(' '*((i*2)-1), end="")
        print('*')
