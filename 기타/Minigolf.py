def calculate_score(N, strokes):
    total_score = 0
    
    for i in range(N):
        par = 2 if (i + 1) % 2 != 0 else 3  # 홀수 번호는 파 2, 짝수 번호는 파 3
        stroke = min(strokes[i], 7)  # 각 코스에서 최대 7타까지만 인정
        total_score += stroke - par  # 타수 - 파를 결과에 누적
    
    return total_score

# 입력
N = int(input().strip())
strokes = list(map(int, input().strip().split()))

# 결과 계산 및 출력
print(calculate_score(N, strokes))
