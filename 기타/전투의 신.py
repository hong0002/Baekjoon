import sys

def solve():
    it = sys.stdin.read().strip().split()
    N = int(it[0])
    A, PA, B, PB = map(int, it[1:5])

    best_val = -1
    best_x = best_y = 0

    # PA <= PB 인 경우: y를 좁은 구간만 순회
    if PA <= PB:
        y_max = N // PB
        delta = B * PA - A * PB  # Δ

        if delta >= 0:
            # 끝쪽 PA개만 확인
            y_start = max(0, y_max - PA + 1)
            y_end = y_max
        else:
            # 처음 PA개만 확인
            y_start = 0
            y_end = min(y_max, PA - 1)

        for y in range(y_start, y_end + 1):
            rem = N - PB * y
            if rem < 0: 
                continue
            x = rem // PA
            val = A * x + B * y
            if val > best_val:
                best_val = val
                best_x, best_y = x, y

    else:
        # PB < PA 인 경우: x를 좁은 구간만 순회 (대칭)
        x_max = N // PA
        delta_prime = A * PB - B * PA  # = -Δ

        if delta_prime >= 0:
            x_start = max(0, x_max - PB + 1)
            x_end = x_max
        else:
            x_start = 0
            x_end = min(x_max, PB - 1)

        for x in range(x_start, x_end + 1):
            rem = N - PA * x
            if rem < 0:
                continue
            y = rem // PB
            val = A * x + B * y
            if val > best_val:
                best_val = val
                best_x, best_y = x, y

    print(best_x, best_y)

if __name__ == "__main__":
    solve()
