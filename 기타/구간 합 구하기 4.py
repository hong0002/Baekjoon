# -*- coding: utf-8 -*-

#수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.


#첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.


#총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

import sys
from collections import deque

num_sum = int(0)

n, m = map(int, input().split())

num = deque()
num = deque(map(int, sys.stdin.readline().split())) # 숫자 리스트 입력
num_range = []

[num_range.append(list(map(int, sys.stdin.readline().split()))) for _ in range(m)] # i, j 리스트 입력

part_sum = deque()
part_sum.append(0) # 부분합 리스트 0으로 초기화

# 부분합 리스트 만들기
for i in range(n):
    num_sum += num.popleft()
    part_sum.append(num_sum)

[print(part_sum[num_range[i][1]] - part_sum[num_range[i][0]-1]) for i in range(m)] # 부분합 출력
