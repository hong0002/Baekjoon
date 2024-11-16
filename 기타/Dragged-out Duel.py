# 입력 처리
n = int(input())
player_choices = input().strip()
guile_choices = input().strip()

# 승리 횟수 초기화
player_wins = 0
guile_wins = 0

# 라운드 비교
for player, guile in zip(player_choices, guile_choices):
    if (player == 'R' and guile == 'S') or (player == 'S' and guile == 'P') or (player == 'P' and guile == 'R'):
        player_wins += 1
    elif (guile == 'R' and player == 'S') or (guile == 'S' and player == 'P') or (guile == 'P' and player == 'R'):
        guile_wins += 1

# 결과 출력
if player_wins > guile_wins:
    print("victory")
else:
    print("defeat")
