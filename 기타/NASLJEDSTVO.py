def find_original_medallions(N, O):
    candidates = []
    # q는 floor(M/N) = {1,2,...,floor(O/(N-1))}
    for q in range(1, O // (N - 1) + 1):
        M = O + q
        if M // N == q:
            candidates.append(M)
    return min(candidates), max(candidates)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input().strip())
    O = int(input().strip())
    lo, hi = find_original_medallions(N, O)
    print(lo, hi)
