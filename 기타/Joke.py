import sys

target = "joke"
ans = 0

for line in sys.stdin:
    # 줄 단위로만 검사 (개행 넘어가는 건 자동으로 배제됨)
    # 겹치는 경우까지 세기 위해 직접 슬라이딩
    for i in range(len(line) - len(target) + 1):
        if line[i:i+4] == target:
            ans += 1

print(ans)
