# 두 팀의 입력 값을 받습니다.
visiting_team = list(map(int, input().split()))
home_team = list(map(int, input().split()))

# 각 팀의 스코어 계산
visiting_score = (visiting_team[0] * 6) + (visiting_team[1] * 3) + (visiting_team[2] * 2) + visiting_team[3] + (visiting_team[4] * 2)
home_score = (home_team[0] * 6) + (home_team[1] * 3) + (home_team[2] * 2) + home_team[3] + (home_team[4] * 2)

# 결과 출력
print(visiting_score, home_score)
