import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    N, M = data[0], data[1]
    Ks = data[2:2+M]

    total = 0
    for x in range(1, N + 1):
        for k in Ks:
            if x % k == 0:
                total += x
                break
    print(total)

if __name__ == "__main__":
    main()
