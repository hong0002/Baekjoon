def check_slot_machine(n, wheels):
    for wheel in wheels:
        if '7' not in wheel:
            return 0
    return 777

# 입력 받기
n = int(input())
wheels = [input().split() for _ in range(3)]

# 슬롯 머신이 좋은지 확인하고 출력
result = check_slot_machine(n, wheels)
print(result)
