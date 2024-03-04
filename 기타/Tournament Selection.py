def determine_group(results):
    wins = results.count('W')
    
    if wins >= 5:
        return 1
    elif wins >= 3:
        return 2
    elif wins >= 1:
        return 3
    else:
        return -1

# 입력 받기
results = [input() for _ in range(6)]

# 결과 출력
print(determine_group(results))
