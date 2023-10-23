# 입력 받기
UR, TR, UO, TO = map(int, input().split())

# site score 계산
site_score = 56 * UR + 24 * TR + 14 * UO + 6 * TO

# 결과 출력
print(site_score)
