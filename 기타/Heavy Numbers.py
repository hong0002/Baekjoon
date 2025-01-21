def calculate_weight(number):
    digits = list(map(int, str(number)))
    return len(digits) * sum(digits)

def compare_weights(a, b):
    weight_a = calculate_weight(a)
    weight_b = calculate_weight(b)

    if weight_a > weight_b:
        return 1
    elif weight_b > weight_a:
        return 2
    else:
        return 0

# 입력 처리
a, b = map(int, input().split())

# 결과 출력
print(compare_weights(a, b))
