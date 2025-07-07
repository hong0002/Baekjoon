def count_discriminative_positions(N, M, spotty, plain):
    count = 0
    for j in range(M):
        S = set()
        P = set()
        # spotty 문자 집합
        for i in range(N):
            S.add(spotty[i][j])
        # plain 문자 집합
        for i in range(N):
            P.add(plain[i][j])
        # 교집합이 없으면 구분 가능한 위치
        if S.isdisjoint(P):
            count += 1
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    spotty = [input().strip() for _ in range(N)]
    plain  = [input().strip() for _ in range(N)]

    result = count_discriminative_positions(N, M, spotty, plain)
    print(result)
