# 입력: 한 줄에 하나씩 (trout, pike, pickerel, total)
trout = int(input().strip())     # Brown Trout 점수
pike = int(input().strip())      # Northern Pike 점수
pickerel = int(input().strip())  # Yellow Pickerel 점수
total = int(input().strip())     # 허용 총점

count = 0
# 가능한 최대 마리 수로 상한을 두고 완전탐색
for bt in range(0, total // trout + 1):
    for np in range(0, total // pike + 1):
        # 현재까지 점수
        used = bt * trout + np * pike
        if used > total:
            continue
        # pickerel 개수는 남은 점수 한도 내에서만 순회
        remaining = total - used
        for yp in range(0, remaining // pickerel + 1):
            if bt == 0 and np == 0 and yp == 0:
                continue  # 최소 1마리 이상 잡아야 함
            score = used + yp * pickerel
            if score <= total:
                print(f"{bt} Brown Trout, {np} Northern Pike, {yp} Yellow Pickerel")
                count += 1

print(f"Number of ways to catch fish: {count}")
