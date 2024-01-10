def calculate_study_time(N, study_times):
    total_time = 0

    for i in range(N):
        total_time += study_times[i]

        # 마지막 계획이 아니라면 휴식 시간 추가
        if i < N - 1:
            total_time += 8

    # 소요 시간을 일과 시간으로 변환
    days = total_time // 24
    hours = total_time % 24

    return days, hours

# 입력 처리
N = int(input())
study_times = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = calculate_study_time(N, study_times)
print(result[0], result[1])
