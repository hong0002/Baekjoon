import sys

def canonical_rotation(s: str) -> str:
    # s의 모든 회전 중 사전순 최소값을 대표로 사용
    return min(s[i:] + s[:i] for i in range(len(s))) if s else s

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    reps = set()
    for _ in range(n):
        w = input().strip()
        reps.add(canonical_rotation(w))
    print(len(reps))

if __name__ == "__main__":
    main()
