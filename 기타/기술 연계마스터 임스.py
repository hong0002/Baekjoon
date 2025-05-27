import sys
input = sys.stdin.readline

N = int(input().strip())
skills = input().strip()

cnt = 0
l_remain = 0  # 'L' 로 남은 사전 스킬 수
s_remain = 0  # 'S' 로 남은 사전 스킬 수
broken = False

for c in skills:
    if broken:
        break
    if '1' <= c <= '9':
        cnt += 1
    elif c == 'L':
        l_remain += 1
    elif c == 'S':
        s_remain += 1
    elif c == 'R':
        if l_remain > 0:
            l_remain -= 1
            cnt += 1
        else:
            broken = True
    elif c == 'K':
        if s_remain > 0:
            s_remain -= 1
            cnt += 1
        else:
            broken = True

print(cnt)
