import sys

def main():
    input = sys.stdin.readline
    B = int(input().strip())
    out = []
    for _ in range(B):
        S, n, f, m = map(int, input().split())
        t = S - m
        if n <= t <= n * f:
            out.append("YES")
        else:
            out.append("NO")
    print("\n".join(out))

if __name__ == "__main__":
    main()
