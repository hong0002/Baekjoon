import sys

N = int(sys.stdin.readline().strip())
words = sys.stdin.readline().strip().split()

print(' '.join(w + 'DORO' for w in words))
