# 입력 받기
P = int(input())

# 각 데이터 세트에 대해 처리
for _ in range(P):
    # 데이터 세트 번호와 N 입력 받기
    K, N = map(int, input().split())
    
    # 계산
    S1 = N * (N + 1) // 2        # 처음 N개의 양의 정수의 합
    S2 = N * N                    # 처음 N개의 홀수 정수의 합
    S3 = N * (N + 1)              # 처음 N개의 짝수 정수의 합
    
    # 결과 출력
    print(K, S1, S2, S3)
