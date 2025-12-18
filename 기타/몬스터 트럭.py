import sys

def main():
    input = sys.stdin.readline
    R, C = map(int, input().split())
    grid = [input().strip() for _ in range(R)]

    ans = [0, 0, 0, 0, 0]  # ans[k] = 2x2에서 X가 k개인 경우의 수

    for i in range(R - 1):
        for j in range(C - 1):
            cells = [
                grid[i][j], grid[i][j+1],
                grid[i+1][j], grid[i+1][j+1]
            ]

            if '#' in cells:
                continue  # 빌딩 있으면 주차 불가

            crushed = cells.count('X')  # 부숴야 하는 차 수
            ans[crushed] += 1

    print("\n".join(map(str, ans)))

if __name__ == "__main__":
    main()
