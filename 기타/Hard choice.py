# 입력을 받습니다.
Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

# 부족한 식사의 개수를 계산합니다.
missing_chicken = max(0, Cr - Ca)
missing_beef = max(0, Br - Ba)
missing_pasta = max(0, Pr - Pa)

# 부족한 식사의 총 개수를 계산합니다.
total_missing = missing_chicken + missing_beef + missing_pasta

# 결과를 출력합니다.
print(total_missing)
