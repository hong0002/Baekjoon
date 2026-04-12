import sys

input = sys.stdin.readline

n = int(input().strip())
pattern = input().strip()

star_idx = pattern.index('*')
prefix = pattern[:star_idx]
suffix = pattern[star_idx + 1:]

for _ in range(n):
    filename = input().strip()

    if len(filename) < len(prefix) + len(suffix):
        print("NE")
    elif filename.startswith(prefix) and filename.endswith(suffix):
        print("DA")
    else:
        print("NE")
