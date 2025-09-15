import sys

def count_k_smooth(N: int, K: int) -> int:
    # 1) 에라토스테네스로 N 이하 소수 구하기
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:N+1:step] = [False] * (((N - start) // step) + 1)

    primes = [i for i in range(2, N + 1) if is_prime[i]]

    # 2) good[x] = True면 x는 현재 K-세준수 후보
    good = [True] * (N + 1)

    # 3) K보다 큰 소수의 배수는 모두 제외
    for p in primes:
        if p > K:
            for m in range(p, N + 1, p):
                good[m] = False

    # 4) 1은 항상 포함, 2..N 중 good인 것 카운트
    return sum(good[1:])

if __name__ == "__main__":
    data = sys.stdin.read().strip().split()
    N = int(data[0])
    K = int(data[1])
    print(count_k_smooth(N, K))
