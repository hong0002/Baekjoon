# 입력을 받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for i in range(1, T + 1):
    # 두 수를 입력받습니다.
    a, b = map(int, input().split())
    
    # 두 수의 합을 구합니다.
    result = a + b
    
    # 결과를 출력합니다.
    print(f"Case {i}: {result}")
