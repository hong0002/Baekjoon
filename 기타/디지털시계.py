import sys

def time_to_sec(s: str) -> int:
    h, m, se = map(int, s.split(':'))
    return h * 3600 + m * 60 + se

def is_multiple_of_3_by_time(t: int) -> bool:
    h = t // 3600
    m = (t % 3600) // 60
    s = t % 60
    return (h + m + s) % 3 == 0

def count_in_range(L: int, R: int) -> int:
    # 구간 [L, R] 에 포함되는 시계 정수 중 3의 배수 개수
    cnt = 0
    if L <= R:
        for t in range(L, R + 1):
            if is_multiple_of_3_by_time(t):
                cnt += 1
    else:
        # 자정(0초)을 넘는 경우: [L, 86399], [0, R]
        for t in range(L, 86400):
            if is_multiple_of_3_by_time(t):
                cnt += 1
        for t in range(0, R + 1):
            if is_multiple_of_3_by_time(t):
                cnt += 1
    return cnt

lines = [line.strip() for line in sys.stdin if line.strip()]
for line in lines:
    start_str, end_str = line.split()
    L = time_to_sec(start_str)
    R = time_to_sec(end_str)
    print(count_in_range(L, R))
