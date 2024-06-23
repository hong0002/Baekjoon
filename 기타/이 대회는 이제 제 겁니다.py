def max_prize(A, P, C):
    # Division 1에서 우승하고 2024 shake!에서 우승하는 경우의 상금 합계
    prize_div1_and_shake = A + C
    
    # Division 2에서 우승하는 경우의 상금
    prize_div2 = P
    
    # 최대 상금을 구합니다.
    max_prize = max(prize_div1_and_shake, prize_div2)
    
    return max_prize

# 입력값을 받습니다.
A, P, C = map(int, input().split())

# 결과를 출력합니다.
print(max_prize(A, P, C))
