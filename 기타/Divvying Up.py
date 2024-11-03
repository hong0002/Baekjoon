def can_distribute_equally(n, winnings):
    total_winnings = sum(winnings)
    
    # 총 상금이 3으로 나누어 떨어지지 않으면 공평한 분배가 불가능
    if total_winnings % 3 != 0:
        return "no"
    else:
        return "yes"

# 입력 처리
n = int(input().strip())
winnings = list(map(int, input().strip().split()))

# 결과 출력
print(can_distribute_equally(n, winnings))
