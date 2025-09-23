import sys

def ok(x, y, X, Y, K):
    if K == 1: return x < X and y == Y
    if K == 2: return x < X and y > Y
    if K == 3: return x == X and y > Y
    if K == 4: return x > X and y > Y
    if K == 5: return x > X and y == Y
    if K == 6: return x > X and y < Y
    if K == 7: return x == X and y < Y
    if K == 8: return x < X and y < Y
    return False

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    logs = [tuple(map(int, input().split())) for _ in range(M)]

    for x in range(1, N+1):
        for y in range(1, N+1):
            good = True
            for X, Y, K in logs:
                # 보물 위치는 관측 위치와 항상 다름
                if x == X and y == Y:
                    good = False
                    break
                if not ok(x, y, X, Y, K):
                    good = False
                    break
            if good:
                print(x, y)
                return

if __name__ == "__main__":
    main()
