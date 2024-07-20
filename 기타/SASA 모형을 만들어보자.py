# 입력 받기
N, M = map(int, input().split())

# SASA 모형의 최대 개수 구하기
max_sasa = min(N // 2, M // 2)

# 결과 출력
print(max_sasa)
