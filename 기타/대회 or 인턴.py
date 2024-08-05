def max_teams(N, M, K):
    # 인턴쉽에 참여하는 학생을 고려하여 남은 학생 수 계산
    while K > 0:
        if N > 2 * M:  # 여학생이 많을 경우 여학생을 인턴쉽에 보냄
            N -= 1
        else:          # 남학생이 많거나 여학생과 남학생의 비율이 맞는 경우 남학생을 인턴쉽에 보냄
            M -= 1
        K -= 1

    # 최대 팀 수 계산
    max_team = min(N // 2, M)
    return max_team

# 입력 받기
N, M, K = map(int, input().split())

# 결과 출력
print(max_teams(N, M, K))
