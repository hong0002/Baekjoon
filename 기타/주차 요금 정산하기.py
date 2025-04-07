import math

# 입력: 기본 요금 A, 단위 시간 B, 추가 요금 C
A, B, C = map(int, input().split())
# 주차 시간 T (분)
T = int(input())

if T <= 30:
    fee = A
else:
    extra_time = T - 30  # 30분 초과 시간
    additional_units = math.ceil(extra_time / B)  # B분마다 계산 (올림)
    fee = A + additional_units * C

print(fee)
