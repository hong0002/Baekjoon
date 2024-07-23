def first_digit_and_length_product(x):
    x_str = str(x)
    first_digit = int(x_str[0])
    length = len(x_str)
    return first_digit * length

def is_fa_number(x):
    seen = set()
    current = x
    
    while current not in seen:
        seen.add(current)
        next_value = first_digit_and_length_product(current)
        if next_value == current:
            return "FA"
        current = next_value
    
    return "NFA"

# 입력을 받습니다.
x = int(input().strip())

# FA 수인지 확인합니다.
result = is_fa_number(x)

# 결과를 출력합니다.
print(result)
