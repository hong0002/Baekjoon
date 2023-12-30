def count_valid_gifticons(N, expiration_dates):
    valid_gifticons = 0

    for date in expiration_dates:
        _, days_left = date.split('-')
        days_left = int(days_left)
        
        if days_left <= 90:
            valid_gifticons += 1

    return valid_gifticons

# 입력 받기
N = int(input())
expiration_dates = []
for _ in range(N):
    expiration_dates.append(input())

# 결과 출력
result = count_valid_gifticons(N, expiration_dates)
print(result)
