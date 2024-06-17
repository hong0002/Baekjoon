def can_hang_cloak(h, l, a, b):
    # 세로줄에 플래그의 한 변을 걸었을 때 바닥에 닿는지 여부를 확인
    if h >= a / 2 and l >= b:
        return "YES"
    if h >= b / 2 and l >= a:
        return "YES"
    return "NO"

# 입력 받기
input_line = input().strip()
h, l, a, b = map(int, input_line.split())

# 결과 출력
print(can_hang_cloak(h, l, a, b))
