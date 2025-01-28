import sys

# 변수로 최저 온도와 최고 온도를 설정합니다.
min_temp = float('inf')
max_temp = float('-inf')

# 입력 처리
for line in sys.stdin:
    # 공백을 기준으로 각 토큰을 분리
    tokens = line.split()
    
    # 첫 번째 토큰은 날짜이므로 온도 값들만 가져옵니다.
    temperatures = list(map(int, tokens[1:]))
    
    # 최저 온도와 최고 온도를 업데이트합니다.
    min_temp = min(min_temp, *temperatures)
    max_temp = max(max_temp, *temperatures)

# 결과 출력
print(min_temp, max_temp)
