# 입력 받기
input_data = input().split()
total_score = int(input_data[0])
score_difference = int(input_data[1])

# 팀의 득점 계산
team1_score = (total_score + score_difference) // 2
team2_score = total_score - team1_score

# 득점이 음수거나 정수가 아닌 경우, 불가능한 경우이므로 -1 출력
if team1_score < 0 or team2_score < 0 or (total_score + score_difference) % 2 != 0:
    print(-1)
else:
    # 결과 출력
    print(team1_score, team2_score)
