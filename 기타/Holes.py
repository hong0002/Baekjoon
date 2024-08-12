def minimal_number_with_holes(h):
    if h == 0:
        return "1"
    elif h == 1:
        return "0"
    else:
        result = ""
        if h % 2 == 1:
            result += "4"  # 홀수를 4로 처리
            h -= 1
        
        # 나머지를 모두 8로 채움
        result += "8" * (h // 2)
        
        return result

# 입력
h = int(input().strip())

# 결과 출력
print(minimal_number_with_holes(h))
