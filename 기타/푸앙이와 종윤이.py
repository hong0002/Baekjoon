def veda_multiplication(x, y):
    a = 100 - x
    b = 100 - y
    c = 100 - (a + b)
    d = a * b

    q = d // 100
    r = d % 100

    # 결과 계산
    result_c = c + q
    result_d = r

    # 출력
    print(a, b, c, d, q, r)
    
    # 앞의 두 자릿수, 뒤의 두 자릿수 출력
    # 십의 자리가 0인 경우, 일의 자리만 출력
    if result_d < 10:
        print(result_c, result_d)
    else:
        print(result_c, result_d)

# 입력 받기
x, y = map(int, input().split())
veda_multiplication(x, y)
