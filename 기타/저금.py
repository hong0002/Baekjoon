import sys

# 입력 전체를 읽어서 각 줄마다 처리
input_data = sys.stdin.read().strip().splitlines()
for line in input_data:
    if not line.strip():
        continue
    # N: 초기 금액, B: 이자율, M: 목표 금액
    N, B, M = map(float, line.split())
    years = 0
    # "M원을 넘게"이므로 M보다 크기 전까지 반복 (M과 같으면 아직 조건 충족 X)
    while N <= M:
        N *= (1 + B/100)
        years += 1
    print(years)
