# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
#
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
#
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys
import math
input = sys.stdin.readline

m, n = map(int, input().split())

array = [True for _ in range(n + 1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if i == 1:
        continue
    if array[i]:
        print(i)
