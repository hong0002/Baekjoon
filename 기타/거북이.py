def largest_rectangle_area(a, b, c, d):
    sides = [a, b, c, d]
    max_area = 0
    
    # 가능한 모든 쌍을 선택하여 직사각형을 만든다.
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(4):
                if k != i and k != j:
                    for l in range(k + 1, 4):
                        if l != i and l != j:
                            width = min(sides[i], sides[j])
                            height = min(sides[k], sides[l])
                            area = width * height
                            max_area = max(max_area, area)
    
    return max_area

# 입력
A, B, C, D = map(int, input().split())

# 가장 큰 직사각형의 면적 계산
result = largest_rectangle_area(A, B, C, D)

# 결과 출력
print(result)
