# 가격 정보
blaster_price = 350.34
visual_sensor_price = 230.90
audio_sensor_price = 190.55
arm_price = 125.30
leg_price = 180.90

# 테스트 케이스 수 입력
t = int(input())

# 각 테스트 케이스에 대해 처리
for _ in range(t):
    # 부품의 개수 입력
    A, B, C, D, E = map(int, input().split())
    
    # 총 비용 계산
    total_cost = (A * blaster_price) + (B * visual_sensor_price) + (C * audio_sensor_price) + (D * arm_price) + (E * leg_price)
    
    # 결과 출력 (소수점 둘째 자리까지)
    print(f"${total_cost:.2f}")
