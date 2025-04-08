def find_first_off_time():
    import sys
    input = sys.stdin.readline
    
    N = int(input().strip())
    # 초기값: 2^31 보다 큰 값 사용 (문제의 조건에 맞춰)
    min_off_time = 2**31  
    for _ in range(N):
        M, O = map(int, input().strip().split())
        if O == 0:  # LED가 꺼진 상태인 경우
            if M < min_off_time:
                min_off_time = M
                
    # LED가 한 번도 꺼지지 않은 경우
    if min_off_time == 2**31:
        print(-1)
    else:
        print(min_off_time)

# 만약 직접 실행하기 위한 코드라면 다음을 사용합니다.
if __name__ == '__main__':
    find_first_off_time()
