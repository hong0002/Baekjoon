# 입력 받기
times = [int(input()) for _ in range(4)]

# 총 시간 계산 (마지막 한 바퀴를 300초에 달린다고 가정)
total_time = sum(times) + 300

# 수행평가 통과 여부 판단
if total_time <= 1800:
    print("Yes")
else:
    print("No")
