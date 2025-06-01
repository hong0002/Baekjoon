import sys
import math

# 입력: 한 줄에 정수 N
N = int(sys.stdin.readline())

# 정답: sqrt(N)의 정수 부분
answer = int(math.isqrt(N))  # Python 3.8 이상에서는 math.isqrt를 쓰면 안전하게 정수 제곱근을 구할 수 있습니다.
print(answer)
