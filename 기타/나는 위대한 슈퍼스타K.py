import sys

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    N = int(next(it)); M = int(next(it)); K = int(next(it))

    max_score = [-10**18] * (N + 1)
    for _ in range(M):
        # 각 줄에 N개의 (i, s) 쌍
        for __ in range(N):
            i = int(next(it))
            s = float(next(it))
            if s > max_score[i]:
                max_score[i] = s

    best = sorted(max_score[1:], reverse=True)
    total = sum(best[:K])
    print(f"{total:.1f}")

if __name__ == "__main__":
    main()
