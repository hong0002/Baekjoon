# -*- coding: utf-8 -*-

#예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.


#첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.


#첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input())

for i in range(n):
    print(' '*(n-i-1), end="")
    print('*'*((i*2)+1))
for i in range(n-1, 0, -1):
    print(' '*(n-i), end="")
    print('*'*(((i-1)*2)+1))
