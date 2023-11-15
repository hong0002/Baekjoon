def calculate_days_to_play(L, A, B, C, D):
    # 국어와 수학 중 더 많이 푼 페이지 수를 구함
    language_pages = (A + C - 1) // C
    math_pages = (B + D - 1) // D

    # 놀 수 있는 날의 최댓값은 방학 기간 L에서 국어와 수학 중 더 적게 푼 페이지 수를 뺀 값
    days_to_play = L - max(language_pages, math_pages)

    return days_to_play

# 입력 받기
L = int(input())  # 방학 기간
A = int(input())  # 국어 페이지 수
B = int(input())  # 수학 페이지 수
C = int(input())  # 하루에 풀 수 있는 국어 페이지 수
D = int(input())  # 하루에 풀 수 있는 수학 페이지 수

# 결과 출력
result = calculate_days_to_play(L, A, B, C, D)
print(result)
