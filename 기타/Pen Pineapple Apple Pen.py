import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()   # 길이 n인 문자열, 'A', 'P', 'p' 로만 이루어져 있음

count = 0
last = -10  # "마지막으로 선택한 패턴의 시작 인덱스" (처음에는 충분히 작은 값)

# 마지막 i는 n-4 까지 (i+3 <= n-1 이어야 하므로)
for i in range(n - 3):
    # 네 글자가 정확히 "pPAp" 인지 확인
    if s[i] == 'p' and s[i+1] == 'P' and s[i+2] == 'A' and s[i+3] == 'p':
        # 만약 i == last+3 이면 앞선 패턴과 펜('p')이 겹치므로 건너뛰기
        if i == last + 3:
            continue
        # 그렇지 않다면 이 패턴을 선택
        count += 1
        last = i

print(count)
