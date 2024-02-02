def find_winner(game_record):
    score_A = 0
    score_B = 0
    win_by_2 = False
    
    for i in range(0, len(game_record), 2):
        player = game_record[i]
        points = int(game_record[i + 1])
        
        if player == 'A':
            score_A += points
        else:
            score_B += points
            
        if score_A >= 11 or score_B >= 11:
            if abs(score_A - score_B) >= 2:
                win_by_2 = True
                break

    if win_by_2:
        if score_A > score_B:
            return 'A'
        else:
            return 'B'
    else:
        if score_A == score_B:
            return game_record[-2]
        elif score_A > score_B:
            return 'A'
        else:
            return 'B'

# 입력 받기
game_record = input().strip()

# 승자 찾기
winner = find_winner(game_record)

# 출력
print(winner)
