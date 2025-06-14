import sys

def is_sator_square(n, grid):
    for i in range(n):
        # i번째 열 문자열 만들기
        col = ''.join(grid[j][i] for j in range(n))
        if grid[i] != col:
            return False
    return True

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    grid = [input().rstrip() for _ in range(n)]
    print("YES" if is_sator_square(n, grid) else "NO")

if __name__ == "__main__":
    main()
