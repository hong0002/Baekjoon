import sys

input = sys.stdin.readline

N = int(input())
rocks = list(map(int, input().split()))

print(N - len(set(rocks)))
