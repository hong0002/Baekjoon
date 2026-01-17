import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())

    max_x1 = max_y1 = max_z1 = -10**18
    min_x2 = min_y2 = min_z2 = 10**18

    for _ in range(N):
        x1, y1, z1, x2, y2, z2 = map(int, input().split())
        if x1 > max_x1: max_x1 = x1
        if y1 > max_y1: max_y1 = y1
        if z1 > max_z1: max_z1 = z1
        if x2 < min_x2: min_x2 = x2
        if y2 < min_y2: min_y2 = y2
        if z2 < min_z2: min_z2 = z2

    dx = min_x2 - max_x1
    dy = min_y2 - max_y1
    dz = min_z2 - max_z1

    if dx <= 0 or dy <= 0 or dz <= 0:
        print(0)
    else:
        print(dx * dy * dz)

if __name__ == "__main__":
    main()
