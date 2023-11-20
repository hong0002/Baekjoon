def check_triangle(a, b, c):
    # 정렬하여 가장 긴 변을 c로 설정
    sides = sorted([a, b, c], reverse=True)
    a, b, c = sides

    # 삼각형의 부등식을 확인하여 조건에 따라 출력
    if a >= b + c:
        return 0  # Bajtuś는 삼각형을 만들 수 없음
    elif a**2 == b**2 + c**2:
        return 1  # Bajtuś는 직각 삼각형을 만들 수 있음
    elif a == b == c:
        return 2  # Bajtuś는 정삼각형을 만들 수 있음
    else:
        return 0  # Bajtuś는 직각 삼각형이나 정삼각형을 만들 수 없음

# 입력 받기
a, b, c = map(int, input().split())

# 결과 출력
result = check_triangle(a, b, c)
print(result)
