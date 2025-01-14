def count_times(N, M):
    count = 0
    while N > 0:
        count += N  # N개의 지폐 또는 묶음을 센다
        N //= M     # N을 M개씩 묶음으로 나눈다
    return count


# 입력 처리
N, M = map(int, input().split())

# 결과 출력
print(count_times(N, M))
