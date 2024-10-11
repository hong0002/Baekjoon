# 입력 받기
N = int(input())

# 승리 횟수를 저장할 변수
wins = 0

# 각 게임에 대해 자동차가 있는 문을 확인
for _ in range(N):
    car_door = int(input())
    # 자동차가 문 1이 아닌 문에 있을 경우 참가자는 변경 후 자동차를 얻음
    if car_door != 1:
        wins += 1

# 결과 출력
print(wins)
