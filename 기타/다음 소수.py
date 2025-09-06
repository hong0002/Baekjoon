import sys

# Miller–Rabin for 32-bit (deterministic with bases {2,3,5,7,11})
def is_prime(n: int) -> bool:
    if n < 2: return False
    small_primes = [2,3,5,7,11]
    for p in small_primes:
        if n % p == 0:
            return n == p
    # write n-1 = d * 2^s with d odd
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in small_primes:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def next_prime(n: int) -> int:
    if n <= 2:
        return 2
    # 홀수로 맞추고 2씩 증가
    n = n if n % 2 == 1 else n + 1
    while True:
        if is_prime(n):
            return n
        n += 2

def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        out_lines.append(str(next_prime(n)))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
