import sys

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    customer = list(map(int, input().split()))
    ans = 0

    for _ in range(n):
        trash = list(map(int, input().split()))
        ok = True
        for c, t in zip(customer, trash):
            if t > c:       # 쓰레기 키가 더 깊으면 절대 못 맞춤
                ok = False
                break
        if ok:
            ans += 1

    print(ans)
