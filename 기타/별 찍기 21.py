# -*- coding: utf-8 -*-

#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.


#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.


#첫째 줄부터 차례대로 별을 출력한다.

n = int(input())

if n % 2 == 0:
    for i in range(n*2):
        if i % 2 == 0:
            print('* '*(n//2))
        else:
            print(' *'*(n//2))
else:
    for i in range(n*2):
        if i % 2 == 0:
            print('* '*((n//2)+1))
        else:
            print(' *'*(n//2))
