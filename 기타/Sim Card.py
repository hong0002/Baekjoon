while True:
    # 학생의 전화 및 데이터 사용량 입력
    c, d = map(int, input().split())
    
    # 종료 조건
    if c == 0 and d == 0:
        break
    
    # 세 개의 운영자에 대해 비용 계산
    cost_parstel = c * 30 + d * 40
    cost_parscell = c * 35 + d * 30
    cost_parsphone = c * 40 + d * 20
    
    # 최소 비용을 출력
    print(min(cost_parstel, cost_parscell, cost_parsphone))
