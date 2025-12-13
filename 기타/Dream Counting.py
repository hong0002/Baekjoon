import sys

def count_0_to_n(n: int):
    """0부터 n까지(포함)에서 각 숫자(0~9)가 등장한 횟수 반환"""
    if n < 0:
        return [0] * 10

    counts = [0] * 10
    factor = 1

    while factor <= n:
        lower = n % factor
        cur = (n // factor) % 10
        higher = n // (factor * 10)

        # 기본: 각 숫자 d가 higher * factor 만큼 반복 등장
        for d in range(10):
            counts[d] += higher * factor

        # 선행 0 보정
        counts[0] -= factor

        # 현재 자리 cur에 따른 추가
        for d in range(10):
            if cur > d:
                counts[d] += factor
            elif cur == d:
                counts[d] += lower + 1

        factor *= 10

    # 숫자 0 자체("0") 포함
    counts[0] += 1
    return counts

def main():
    data = sys.stdin.read().strip().split()
    M, N = map(int, data)

    a = count_0_to_n(N)
    b = count_0_to_n(M - 1)
    ans = [a[i] - b[i] for i in range(10)]
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
