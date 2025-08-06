import sys
import math

def main():
    X1, Y1, R1 = map(int, sys.stdin.readline().split())
    X2, Y2, R2 = map(int, sys.stdin.readline().split())

    dx = X1 - X2
    dy = Y1 - Y2
    # 중심 거리의 제곱
    dist2 = dx*dx + dy*dy

    sumR = R1 + R2
    diffR = abs(R1 - R2)
    sumR2 = sumR * sumR
    diffR2 = diffR * diffR

    # 두 원이 완전히 일치하는 경우 (중심도 같고, 반지름도 같음)
    if dist2 == 0 and R1 == R2:
        print("YES")
        return

    # 외접 혹은 내접(한 점)인 경우
    if dist2 == sumR2 or dist2 == diffR2:
        print("NO")
        return

    # centers too far apart
    if dist2 > sumR2:
        print("NO")
        return

    # one inside other without touching or intersecting in two points
    # dist2 < diffR2  → 완전 내포
    # diffR2 < dist2 < sumR2 → 두 점에서 교차
    if dist2 < sumR2 and (dist2 < diffR2 or dist2 > diffR2):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
