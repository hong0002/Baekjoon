import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
S = [int(input()) for _ in range(n-1)]

has_a = any(x == a for x in S)
has_b = any(x == b for x in S)

candidates = []
if has_a and has_b:
    # 이미 S 안에 a, b 둘 다 등장 → 빠진 날은 a~b 중 아무거나 가능
    candidates = list(range(a, b+1))
elif not has_a and not has_b:
    # S 안에 a도 없고 b도 없다 → 하루로는 동시에 a와 b를 채울 방법이 없음
    candidates = []
elif not has_a and has_b:
    # a가 빠져 있으므로 빠진 날에 반드시 a를 넣어야 함
    candidates = [a]
else:  # has_a == True and has_b == False
    # b가 빠져 있으므로 빠진 날에 반드시 b를 넣어야 함
    candidates = [b]

if not candidates:
    print(-1)
else:
    for w in candidates:
        print(w)
