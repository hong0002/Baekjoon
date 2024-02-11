def character_type(preliminary, final):
    v = preliminary / final

    if v < 0.2:
        return "weak"
    elif 0.2 <= v < 0.4:
        return "normal"
    elif 0.4 <= v < 0.6:
        return "strong"
    else:
        return "very strong"

# 입력 받기
p_x, r_x = map(int, input().split())

# character_type 함수 호출 및 결과 출력
result = character_type(p_x, r_x)
print(result)
