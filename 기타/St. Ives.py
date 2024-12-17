while True:
    # 입력 받기
    W = float(input())

    # 종료 조건
    if W == 0:
        break
    
    # 총합 계산
    total = 1 + W + W**2 + W**3 + W**4

    # 결과 출력
    print(f"{total:.2f}")
