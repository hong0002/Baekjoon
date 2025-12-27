import sys

def main():
    input = sys.stdin.readline
    N, M, Q = map(int, input().split())

    chars = [input().strip() for _ in range(N)]

    # constraints[i] = 'Y' or 'N' if attribute i is constrained, else None
    constraints = [None] * M
    for _ in range(Q):
        a, yn = input().split()
        a = int(a) - 1
        constraints[a] = yn

    cnt = 0
    last_idx = -1

    for i, s in enumerate(chars):
        ok = True
        for j in range(M):
            c = constraints[j]
            if c is not None and s[j] != c:
                ok = False
                break
        if ok:
            cnt += 1
            last_idx = i + 1  # 1-based index

    if cnt == 1:
        print("unique")
        print(last_idx)
    else:
        print("ambiguous")
        print(cnt)

if __name__ == "__main__":
    main()
