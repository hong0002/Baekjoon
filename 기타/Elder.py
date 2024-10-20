# 입력 받기
current_wizard = input().strip()  # 처음에 지팡이가 따르는 마법사
N = int(input().strip())  # 대결의 횟수

# 지팡이가 따르게 된 마법사들을 기록할 집합
wizards_obeyed = {current_wizard}

# 각 대결 처리
for _ in range(N):
    winner, loser = input().split()
    
    # 현재 지팡이가 따르는 마법사가 패배하면, 승리한 마법사를 따르게 된다
    if loser == current_wizard:
        current_wizard = winner
        wizards_obeyed.add(current_wizard)

# 출력
print(current_wizard)  # 마지막에 지팡이가 따르는 마법사
print(len(wizards_obeyed))  # 지팡이가 따르게 된 서로 다른 마법사의 수
