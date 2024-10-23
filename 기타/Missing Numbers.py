# 입력 받기
n = int(input())
recited_numbers = [int(input()) for _ in range(n)]

# 1부터 마지막 숫자까지 중 빠진 숫자를 찾아 출력
missing_numbers = []
for i in range(1, recited_numbers[-1] + 1):
    if i not in recited_numbers:
        missing_numbers.append(i)

# 결과 출력
if not missing_numbers:
    print("good job")
else:
    for number in missing_numbers:
        print(number)
