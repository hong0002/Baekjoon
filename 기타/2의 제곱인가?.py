import sys

n = int(sys.stdin.readline().strip())
print(1 if n > 0 and (n & (n - 1)) == 0 else 0)
