def is_november_day(A, B):
    # 2022년 11월의 일수
    november_days = 30
    
    # A일로부터 B주 후의 날짜를 계산
    target_day = A + (7 * B)
    
    # 해당 날짜가 2022년 11월인지 여부 확인
    if 1 <= target_day <= november_days:
        return 1
    else:
        return 0

# 입력 받기
A = int(input())
B = int(input())

# 결과 출력
result = is_november_day(A, B)
print(result)
