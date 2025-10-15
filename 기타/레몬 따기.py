import sys

input=sys.stdin.readline
N=int(input().strip())
a=list(map(int,input().split()))

ans=0
for i, v in enumerate(a, start=1):
    keep = v - ((N+1) - i)
    if keep > ans:
        ans = keep
print(max(0, ans))
