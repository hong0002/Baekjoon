def stopwatch_display(N, times):
    # 만약 버튼 누름 횟수가 홀수라면, 타이머는 아직 실행 중
    if N % 2 != 0:
        return "still running"
    
    total_time = 0
    # 짝수 쌍을 묶어서 시간 계산
    for i in range(0, N, 2):
        total_time += times[i + 1] - times[i]
    
    return total_time

# 입력 예제
N = int(input())
times = [int(input()) for _ in range(N)]

# 함수 호출 및 결과 출력
result = stopwatch_display(N, times)
print(result)
