# -*- coding: utf-8 -*-

#오각형의 각 변에 아래 그림과 같이 점을 찍어 나간다. N단계에서 점의 개수는 모두 몇 개일까?


#첫째 줄에 N(1 ≤ N ≤ 10,000,000)이 주어진다.


#첫째 줄에 N단계에서 점의 개수를 45678로 나눈 나머지를 출력한다.

point_count = (5)
n = int(input())

if n == 1:
    print(point_count % 45678)
else:
    for i in range(n-1):
        point_count = point_count + 7 + 3*i
    print(point_count % 45678)
