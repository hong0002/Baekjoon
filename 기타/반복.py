import sys

S = sys.stdin.readline().strip()

K = 1
prev = -1  # 직전 선택 문자의 알파벳 인덱스 (-1은 시작 전)

for ch in S:
    pos = ord(ch) - ord('a')
    if pos > prev:
        prev = pos
    else:
        K += 1
        prev = pos

print(K)
