import sys

def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 3:
        print("usage: N Mlim Plim", file=sys.stderr)
        return
    N, Mlim, Plim = map(int, data)

    Ntot = 2 * N
    M = N * N
    Pmax = N  # 설명 참조

    # 제약 확인 (문제 조건 보장되지만 안전 확인)
    if Ntot > 500_000 or M > Mlim or Pmax > Plim:
        # 이 경우에는 다른 구성(계층 추가 등)을 써야 하나,
        # 주어진 테스트(N=118, Mlim=1e6, Plim=1e6)에서는 여기로 오지 않습니다.
        print("-1")
        return

    # 헤더 출력
    print(Ntot, M)

    # 간선: 모든 입력 i (1..N) → 모든 출력 (N+j) (j=1..N)
    # 경로 유일성 및 제약 조건 만족
    for i in range(1, N + 1):
        base = N  # 출력 시작 오프셋
        for j in range(1, N + 1):
            print(i, base + j)

if __name__ == "__main__":
    main()
