# 입력 받기
S_price, S_weight = map(int, input().split())
N_price, N_weight = map(int, input().split())
U_price, U_weight = map(int, input().split())

# 가성비 계산 함수
def calculate_value(price, weight):
    total_price = price * 10
    if total_price >= 5000:
        total_price -= 500
    total_weight = weight * 10
    return total_weight / total_price

# 각 과자의 가성비 계산
S_value = calculate_value(S_price, S_weight)
N_value = calculate_value(N_price, N_weight)
U_value = calculate_value(U_price, U_weight)

# 최고 가성비를 가진 과자 선택
if S_value > N_value and S_value > U_value:
    print("S")
elif N_value > S_value and N_value > U_value:
    print("N")
else:
    print("U")
