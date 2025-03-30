n = int(input())
numbers = [int(input()) for _ in range(n)]
i = 0

while i < n:
    base = numbers[i]  # 새로운 라운드의 첫 번째 숫자
    i += 1
    while i < n:
        if numbers[i] % base == 0:
            print(numbers[i])
            i += 1
            break  # 배수를 찾았으므로 현재 라운드 종료
        i += 1
