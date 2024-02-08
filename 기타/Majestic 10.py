def count_doubles(stats):
    count = 0
    for stat in stats:
        if stat >= 10:
            count += 1
    return count

def print_result(stats):
    print(' '.join(map(str, stats)))
    doubles_count = count_doubles(stats)

    if doubles_count == 0:
        print('zilch')
    elif doubles_count == 1:
        print('double')
    elif doubles_count == 2:
        print('double-double')
    elif doubles_count == 3:
        print('triple-double')

    print()  # Leave a blank line after the output

# 입력 받기
n = int(input())
for _ in range(n):
    player_stats = list(map(int, input().split()))
    print_result(player_stats)
