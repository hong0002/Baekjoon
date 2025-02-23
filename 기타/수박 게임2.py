def max_watermelons(N, K):
    cherries = K
    for i in range(1, N):
        # i단계 과일을 만들기 위해 i단계 과일 수에 2를 곱해야 한다.
        if cherries < 2:
            return 0  # 더 이상 과일을 만들 수 없으면 종료
        cherries //= 2  # 두 개씩 소모하여 한 개를 만들므로 2로 나눔
    return cherries

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(max_watermelons(N, K))
