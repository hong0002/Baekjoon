# 입력받은 세 점수를 공백으로 구분하여 입력 받습니다.
A, B, C = map(int, input().split())

# 세 점수를 리스트에 담고 내림차순으로 정렬합니다.
scores = [A, B, C]
scores.sort(reverse=True)

# 가장 높은 두 점수를 합산합니다.
result = scores[0] + scores[1]

# 결과를 출력합니다.
print(result)
