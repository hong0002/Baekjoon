def sum_of_digits(x):
    return sum(int(digit) for digit in str(x))

def find_smallest_harshad(n):
    while True:
        if n % sum_of_digits(n) == 0:
            return n
        n += 1

# 입력 받기
n = int(input())

# 결과 출력
print(find_smallest_harshad(n))
