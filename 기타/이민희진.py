import sys

input = sys.stdin.readline

N = int(input().strip())
names = [input().strip() for _ in range(N)]


def can_connect(a: str, b: str) -> bool:
    L = min(len(a), len(b))
    for k in range(1, L + 1):
        # a 앞 k == b 뒤 k
        if a[:k] == b[-k:]:
            return True
        # a 뒤 k == b 앞 k
        if a[-k:] == b[:k]:
            return True
    return False


ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if can_connect(names[i], names[j]):
            ans += 1

print(ans)
