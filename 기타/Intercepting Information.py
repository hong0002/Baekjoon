# 8개의 정수 입력 받기
n_values = list(map(int, input().split()))

# 9가 있는지 확인
if 9 in n_values:
    print("F")  # 9가 있으면 실패 출력
else:
    print("S")  # 9가 없으면 성공 출력
