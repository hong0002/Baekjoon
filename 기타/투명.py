import sys

def main():
    input=sys.stdin.readline
    N, M = map(int, input().split())
    # 좌표가 1..100, x2+1, y2+1 처리를 위해 102×102 사용
    imos = [[0]*102 for _ in range(102)]

    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        imos[x1][y1] += 1
        imos[x2+1][y1] -= 1
        imos[x1][y2+1] -= 1
        imos[x2+1][y2+1] += 1

    # 누적합 (x, y 각각 1..100까지만 결과 사용)
    for x in range(1, 101):
        for y in range(1, 101):
            imos[x][y] += imos[x-1][y] + imos[x][y-1] - imos[x-1][y-1]

    # M개 이하면 '보임', M 초과면 '안 보임'
    ans = sum(1 for x in range(1, 101) for y in range(1, 101) if imos[x][y] > M)
    print(ans)

if __name__ == "__main__":
    main()
