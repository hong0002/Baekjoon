n, m = map(int, input().split())
for D in range(28, 32):
    # m에서 7일 후의 날짜 계산 (달을 넘으면 wrap-around)
    if m + 7 <= D:
        L = m + 7
    else:
        L = m + 7 - D
    # 지난 일요일에서 7일 후(오늘)가 n과 일치하는지 확인
    if L + 7 <= D:
        today = L + 7
    else:
        today = L + 7 - D
    if today == n:
        print(L)
        break
Rain Diary
