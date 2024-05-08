def find_last_round(rank):
    if rank <= 25:
        return "World Finals"
    elif rank <= 1000:
        return "Round 3"
    elif rank <= 4500:
        return "Round 2"
    else:
        return "Round 1"

# 입력을 받을 테스트 케이스의 수
T = int(input().strip())

# 각 테스트 케이스에 대해
for case_number in range(1, T + 1):
    # 참가자가 마지막으로 참가한 라운드의 등수 N
    N = int(input().strip())
    # 마지막으로 참가한 라운드 결정
    last_round = find_last_round(N)
    # 형식에 맞게 출력
    print(f"Case #{case_number}: {last_round}")
