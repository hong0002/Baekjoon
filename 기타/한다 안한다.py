def decision(s: str) -> str:
    m = len(s) // 2
    return "Do-it" if s[m-1] == s[m] else "Do-it-Not"

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    for _ in range(N):
        s = input().strip()
        print(decision(s))
