import sys

MOD = 1_000_000_007

def main():
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    ns = [int(next(it)) for _ in range(t)]
    maxn = max(ns) if ns else 0

    # factorial[0..maxn]
    fact = [1] * (maxn + 1)
    for i in range(2, maxn + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    out = []
    for n in ns:
        ans = (fact[n] - 1) % MOD   # n! - 1 (mod MOD)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    main()
