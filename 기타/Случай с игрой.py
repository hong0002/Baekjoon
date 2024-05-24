# 입력을 받습니다.
n, k = map(int, input().split())
actions = [input().strip() for _ in range(n)]

# 초기화
current_ammo = 0
saved_ammo = 0

# 각 행동에 따라 처리합니다.
for action in actions:
    if action == "save":
        saved_ammo = current_ammo
    elif action == "load":
        current_ammo = saved_ammo
    elif action == "shoot":
        if current_ammo > 0:
            current_ammo -= 1
    elif action == "ammo":
        current_ammo += k
    
    # 결과 출력
    print(current_ammo)
