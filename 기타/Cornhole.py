# 입력 받기
player1_input = input().split()
player2_input = input().split()

# 입력 값 추출
H1, B1 = map(int, player1_input)
H2, B2 = map(int, player2_input)

# 취소 스코어 계산
score1 = 3 * H1 + B1
score2 = 3 * H2 + B2

# 결과 출력
if score1 > score2:
    print("1", score1 - score2)
elif score2 > score1:
    print("2", score2 - score1)
else:
    print("NO SCORE")
