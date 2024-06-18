def better_dice(n, first_die, second_die):
    first_wins = 0
    second_wins = 0
    
    for i in range(n):
        for j in range(n):
            if first_die[i] > second_die[j]:
                first_wins += 1
            elif first_die[i] < second_die[j]:
                second_wins += 1

    if first_wins > second_wins:
        return "first"
    elif second_wins > first_wins:
        return "second"
    else:
        return "tie"

# 입력 받기
n = int(input().strip())
first_die = list(map(int, input().strip().split()))
second_die = list(map(int, input().strip().split()))

# 결과 출력
print(better_dice(n, first_die, second_die))
