def shifty_sum(N: int, k: int) -> int:
    total = 0
    current = N
    for _ in range(k + 1):
        total += current
        current *= 10
    return total

if __name__ == "__main__":
    N = int(input().strip())
    k = int(input().strip())
    print(shifty_sum(N, k))
