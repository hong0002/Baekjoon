import sys
input = sys.stdin.readline

def intersection_count(x1, y1, r1, x2, y2, r2):
    dx = x2 - x1
    dy = y2 - y1
    d2 = dx*dx + dy*dy
    # 중심이 같은 경우
    if d2 == 0:
        return -1 if r1 == r2 else 0
    sum_r = r1 + r2
    diff_r = abs(r1 - r2)
    sum_r2 = sum_r * sum_r
    diff_r2 = diff_r * diff_r
    # 교점 개수 판정
    if d2 > sum_r2:
        return 0
    elif d2 < diff_r2:
        return 0
    elif d2 == sum_r2 or d2 == diff_r2:
        return 1
    else:
        return 2

def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(intersection_count(x1, y1, r1, x2, y2, r2))

if __name__ == "__main__":
    main()
