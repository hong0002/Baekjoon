def check_luckiness(number):
    contains_seven = '7' in str(number)
    divisible_by_seven = number % 7 == 0

    if not contains_seven and not divisible_by_seven:
        return 0
    elif not contains_seven and divisible_by_seven:
        return 1
    elif contains_seven and not divisible_by_seven:
        return 2
    else:
        return 3


# 입력 처리
number = int(input().strip())

# 결과 출력
print(check_luckiness(number))
