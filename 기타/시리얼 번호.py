import sys

input = sys.stdin.readline

def digit_sum(s: str) -> int:
    total = 0
    for ch in s:
        if ch.isdigit():
            total += int(ch)
    return total

n = int(input().strip())
serials = [input().strip() for _ in range(n)]

# 정렬 기준: (길이, 숫자합, 사전순)
serials.sort(key=lambda s: (len(s), digit_sum(s), s))

print("\n".join(serials))
