import sys
input = sys.stdin.readline

while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0:
        break

    # 등차 여부 판별
    if a2 - a1 == a3 - a2:
        d = a2 - a1
        print("AP", a3 + d)
    else:
        # 등비수열
        r = a2 // a1
        print("GP", a3 * r)
