while True:
    s = input().strip()
    if s == "0":  # 입력이 0이면 종료
        break
    num = int(s)
    sequence = []  # 진행과정을 저장할 리스트
    while True:
        sequence.append(str(num))
        if num < 10:  # 한 자리 숫자이면 종료
            break
        prod = 1
        for ch in str(num):
            prod *= int(ch)
        num = prod
    print(" ".join(sequence))
