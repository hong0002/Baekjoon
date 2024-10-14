while True:
    # 입력 받기
    income = int(input())
    
    # 입력이 0이면 종료
    if income == 0:
        break
    
    # 세금 계산
    if income <= 1000000:
        tax = 0
    elif income <= 5000000:
        tax = income * 0.1
    else:
        tax = income * 0.2
    
    # 순소득 계산
    net_income = int(income - tax)
    
    # 결과 출력
    print(net_income)
