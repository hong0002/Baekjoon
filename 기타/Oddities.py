# 테스트 케이스의 개수 입력
num_test_cases = int(input())

# 각 테스트 케이스에 대한 루프
for _ in range(num_test_cases):
    # 입력 숫자 받기
    num = int(input())
    
    # 숫자가 짝수인지 홀수인지 판별하여 출력
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
