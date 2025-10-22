import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

t1 = A + C  # 한양대역 경로
t2 = B + D  # 용답역 경로

if t1 < t2:
    print("Hanyang Univ.")
elif t1 > t2:
    print("Yongdap")
else:
    print("Either")
