# Given two integers, calculate and output their sum.
#
#
# The input contains several test cases. The first line contains and integer t (t ≤ 100) denoting the number of test cases. Then t tests follow, each of them consisiting of two space separated integers x and y (−109 ≤ x, y ≤ 109).
#
#
# For each test case output output the sum of the corresponding integers.

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    print(x + y)
