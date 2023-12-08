def min_cctv_count(R, C, N):
    # 한 대의 CCTV가 수용할 수 있는 범위
    coverage = N * N
    
    # 모든 좌석을 커버할 수 있는 최소 CCTV의 개수 계산
    rows_covered = (R + N - 1) // N
    cols_covered = (C + N - 1) // N
    total_cctv_count = rows_covered * cols_covered
    
    return total_cctv_count

# 입력 받기
R, C, N = map(int, input().split())

# 결과 출력
result = min_cctv_count(R, C, N)
print(result)
