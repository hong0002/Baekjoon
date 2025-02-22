def max_watermelons(N, K):
    cherries = K  # 시작 체리 수
    for i in range(1, N):
        if cherries < 2:
            return 0
        cherries //= 2  # i단계 과일을 만들기 위해 2개씩 사용
    return cherries  # N단계 과일(수박)을 만드는 데 남은 체리 개수가 수박의 개수

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(max_watermelons(N, K))
