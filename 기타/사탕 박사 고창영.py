import sys

def main():
    lines = sys.stdin.read().splitlines()
    idx = 0

    # 첫 유효 줄에서 t 읽기
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    t = int(lines[idx].strip())
    idx += 1

    out = []
    for _ in range(t):
        # 테스트케이스 사이 빈 줄 스킵
        while idx < len(lines) and lines[idx].strip() == "":
            idx += 1

        r, c = map(int, lines[idx].split())
        idx += 1

        grid = []
        for _ in range(r):
            grid.append(lines[idx].rstrip("\n"))
            idx += 1

        cnt = 0

        # 가로: >o<
        if c >= 3:
            for i in range(r):
                row = grid[i]
                for j in range(c - 2):
                    if row[j:j+3] == ">o<":
                        cnt += 1

        # 세로: v o ^
        if r >= 3:
            for i in range(r - 2):
                for j in range(c):
                    if grid[i][j] == 'v' and grid[i+1][j] == 'o' and grid[i+2][j] == '^':
                        cnt += 1

        out.append(str(cnt))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
