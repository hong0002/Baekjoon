# 10개의 숫자를 입력받습니다.
numbers = [int(input()) for _ in range(10)]

# 전체 합을 계산합니다.
total_sum = sum(numbers)

# 각 숫자를 한 번씩 제거하면서 나머지 숫자의 합이 현재 숫자와 일치하는지 확인합니다.
for number in numbers:
    if total_sum - number == number:
        print(number)
        break
