import sys
from collections import Counter

def min_erasures(s: str) -> int:
    cnt = Counter(s.strip())
    top2 = sorted(cnt.values(), reverse=True)[:2]
    keep = sum(top2) if top2 else 0
    return len(s.strip()) - keep

def main():
    input_data = sys.stdin.read().strip().splitlines()
    n = int(input_data[0])
    for i in range(1, n+1):
        s = input_data[i]
        print(min_erasures(s))

if __name__ == "__main__":
    main()
