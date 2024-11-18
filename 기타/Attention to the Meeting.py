# 입력 받기
N = int(input())
K = int(input())

# 최대 발언 시간 계산
max_speech_time = (K - (N - 1)) // N

# 출력
print(max_speech_time)
