def calculate_final_score(P, C):
    # 패키지를 배달하여 얻는 점수
    package_points = P * 50
    # 장애물과 충돌하여 잃는 점수
    collision_points = C * 10
    # 패키지 수가 장애물 충돌 수보다 많으면 보너스 점수 획득
    if P > C:
        bonus_points = 500
    else:
        bonus_points = 0
    # 최종 점수 계산
    final_score = package_points - collision_points + bonus_points
    return final_score

# 입력값 받기
P = int(input())
C = int(input())

# 함수 호출하여 결과 출력
print(calculate_final_score(P, C))
