# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대해 반복
for _ in range(T):
    # 문제의 수 입력
    N = int(input())
    
    # 문제의 수만큼 반복하여 두 수를 입력받고, 합과 곱을 출력
    for _ in range(N):
        # 두 수 입력
        Ai, Bi = map(int, input().split())
        
        # 합과 곱 계산 후 출력
        addition = Ai + Bi
        multiplication = Ai * Bi
        print(addition, multiplication)
