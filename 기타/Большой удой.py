# 입력 받기
L = int(input())
T = int(input())

# 두 플레이어가 모두 T초 동안 농업하는 경우, 총 얼마나 농업하는지 계산
total_milk = 2 * T

# 두 플레이어가 총 L 리터를 농업할 때, 승자의 양을 계산
winner_milk = total_milk - L

# 결과 출력
print(winner_milk)
