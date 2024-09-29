# 테스트 케이스 수 입력받기
t = int(input())

# 테스트 케이스 반복
for _ in range(t):
    # 무게의 수 입력받기
    n = int(input())
    
    # 무게 위치 입력받기
    weights = list(map(int, input().split()))
    
    # 왼쪽 토크와 오른쪽 토크를 계산할 변수
    left_torque = 0
    right_torque = 0
    
    # 각 무게에 대해 토크 계산
    for w in weights:
        if w < 0:  # 왼쪽에 위치한 무게
            left_torque += abs(w) * 100  # 음수 거리의 절대값 사용
        elif w > 0:  # 오른쪽에 위치한 무게
            right_torque += w * 100
    
    # 토크 비교하여 결과 출력
    if left_torque > right_torque:
        print("Left")
    elif right_torque > left_torque:
        print("Right")
    else:
        print("Equilibrium")
