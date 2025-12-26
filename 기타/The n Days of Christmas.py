import sys

def total_gifts(n: int) -> int:
    # n(n+1)(n+2)/6 를 오버플로 없이 정수로 계산 (다른 언어에도 안전한 방식)
    a, b, c = n, n + 1, n + 2

    # /2 처리
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2

    # /3 처리
    if a % 3 == 0:
        a //= 3
    elif b % 3 == 0:
        b //= 3
    else:
        c //= 3

    return a * b * c

def main():
    data = sys.stdin.buffer.read().split()
    out = []
    for x in data:
        n = int(x)
        if n == 0:
            break
        out.append(str(total_gifts(n)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
