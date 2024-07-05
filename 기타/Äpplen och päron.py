def who_earned_more(A, P):
    # 사과와 배의 가격
    apple_price = 7
    pear_price = 13
    
    # 각각의 수익 계산
    axel_earnings = A * apple_price
    petra_earnings = P * pear_price
    
    # 비교하여 결과 출력
    if axel_earnings > petra_earnings:
        return "Axel"
    elif axel_earnings < petra_earnings:
        return "Petra"
    else:
        return "lika"

# 입력
A, P = map(int, input().split())

# 결과 출력
print(who_earned_more(A, P))
