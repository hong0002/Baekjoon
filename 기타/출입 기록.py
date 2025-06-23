import sys
input = sys.stdin.readline

N = int(input())
MAX_ID = 200_000

inside = [False] * (MAX_ID + 1)
inside_count = 0
ans = 0

for _ in range(N):
    a, b = map(int, input().split())
    if b == 1:
        # 입장 기록
        if inside[a]:
            # 이미 안에 있으므로, 빠진 퇴장 기록
            ans += 1
            inside[a] = False
            inside_count -= 1
        # 정상 입장 처리
        inside[a] = True
        inside_count += 1
    else:
        # 퇴장 기록
        if not inside[a]:
            # 안에 없으므로, 빠진 입장 기록
            ans += 1
            inside[a] = True
            inside_count += 1
        # 정상 퇴장 처리
        inside[a] = False
        inside_count -= 1

# 로그 종료 후 남아 있는 사람들만큼 퇴장 기록이 빠진 것
ans += inside_count

print(ans)
