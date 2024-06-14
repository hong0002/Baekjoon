import math
import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = int(data[1])
    times = list(map(int, data[2:2+n]))
    
    # 가장 느린 실행 시간
    max_time = max(times)
    
    # 최소 시간 제한 계산 (밀리초를 초로 변환)
    required_time = max_time * s
    time_limit_seconds = math.ceil(required_time / 1000)
    
    # 결과 출력
    print(time_limit_seconds)

# 함수 호출
main()
