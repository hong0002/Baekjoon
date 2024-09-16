# 입력 받기
W, N, P = map(int, input().split())
punches = list(map(int, input().split()))

# 공정한 주먹의 개수 계산
fair_punches = 0
for height in punches:
    if W <= height <= N:
        fair_punches += 1

# 결과 출력
print(fair_punches)
