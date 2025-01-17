def binary_multiplication(B1, B2):
    # 입력 이진수를 10진수로 변환하여 곱셈 수행
    result = int(B1, 2) * int(B2, 2)
    # 결과를 이진수로 변환 후 반환
    return bin(result)[2:]

# 입력 처리
B1 = input().strip()
B2 = input().strip()

# 결과 출력
print(binary_multiplication(B1, B2))
