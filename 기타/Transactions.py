while True:
    # 입력 받기
    balance, action, amount = input().split()
    balance = int(balance)
    amount = int(amount)
    
    # 종료 조건
    if balance == 0 and action == 'W' and amount == 0:
        break
    
    if action == 'W':
        # 인출을 처리
        if balance - amount < -200:
            print("Not allowed")
        else:
            balance -= amount
            print(balance)
    elif action == 'D':
        # 입금을 처리
        balance += amount
        print(balance)
