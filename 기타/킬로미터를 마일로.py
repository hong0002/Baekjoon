import sys

def solve():
    input = sys.stdin.readline

    # 1) 피보나치 수 미리 계산 (F1=1, F2=2; 25000 이하)
    fib = [1, 2]
    while fib[-1] + fib[-2] <= 25000:
        fib.append(fib[-1] + fib[-2])

    t = int(input())
    out_lines = []
    for _ in range(t):
        x = int(input())

        # 2) Zeckendorf 표현 b(x) 계산 (상위 자리부터)
        b = []
        n = x
        started = False
        for f in reversed(fib):
            if f <= n:
                b.append(1)
                n -= f
                started = True
            elif started:
                b.append(0)
        # 이제 b는 (bk, bk-1, ..., b1) 형태의 리스트

        # 3) 오른쪽으로 한 비트 시프트: 마지막 비트 제거
        if b:
            b = b[:-1]  # b(y)

        # 4) b(y)를 값으로 환산
        # b는 여전히 상위비트→하위비트 순서이므로 뒤집어서 fib와 인덱스 매칭
        y = 0
        for i, bit in enumerate(reversed(b)):  # bit가 b1부터 시작
            if bit:
                y += fib[i]  # fib[0]=F1, fib[1]=F2, ...

        out_lines.append(str(y))

    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
