# It is not hard to draw a triangle of stars of any given size. For example, a size 5 triangle would look like this (5 stars high and 5 stars wide):
#
# *
# **
# ***
# ****
# *****
# Your task is to draw triangles in a number of sizes.
#
#
# Each line of input contains a single positive integer, n, 1 <= n <= 100. The last line of input contains 0. For each non-zero number, draw a triangle of that size.
#
#
# Output consists of triangles of the appropriate sizes. Each triangle is wider at the bottom. There are no gaps between the triangles.

while True:
    size = int(input())
    if size == 0:
        break
    for i in range(1, size+1):
        print('*'*i)
