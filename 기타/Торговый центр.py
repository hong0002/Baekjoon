def earliest_arrival_time(n, bus_schedule):
    min_time = float('inf')
    
    for t, l in bus_schedule:
        total_time = t + l
        if total_time < min_time:
            min_time = total_time
    
    return min_time

# 입력 받기
n = int(input())
bus_schedule = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(earliest_arrival_time(n, bus_schedule))
