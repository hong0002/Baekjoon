# 입력 받기
beer, malt, wine, carbonated, seltzer, water = map(int, input().split())

# 각 항목의 병 개수에 대해 5센트를 곱하고 합산
total_refund = 5 * (beer + malt + wine + carbonated + seltzer + water)

# 결과 출력
print(total_refund)
