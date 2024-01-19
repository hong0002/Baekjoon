def calculate_input_difficulty(emoji):
    length = len(emoji)
    colons = emoji.count(':')
    underscores = emoji.count('_')
    
    difficulty = length + colons + underscores * 5
    return difficulty

# 입력 받기
emoji = input().strip()

# 입력 난이도 계산하고 출력
difficulty = calculate_input_difficulty(emoji)
print(difficulty)

