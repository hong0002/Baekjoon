# 입력 받기
a = int(input())

# switch-payout-ratio 계산
ratio_option_one = 100 / a
ratio_option_two = 100 / (100 - a)

# 출력
print("{:.10f}".format(ratio_option_one))
print("{:.10f}".format(ratio_option_two))
