import sys

input = sys.stdin.readline

M, N = map(int, input().split())

prefixes = set()

# phrase book의 모든 prefix 저장
for _ in range(M):
    phrase = input().rstrip('\n')
    for i in range(1, len(phrase) + 1):
        prefixes.add(phrase[:i])

# 메시지가 prefix인지 확인
count = 0
for _ in range(N):
    message = input().rstrip('\n')
    if message in prefixes:
        count += 1

print(count)
