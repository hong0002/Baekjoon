def is_congruent(p1, q1, p2, q2):
    # p1 * p2가 2 * q1 * q2로 나누어떨어지는지 확인
    numerator = p1 * p2
    denominator = 2 * q1 * q2
    
    if numerator % denominator == 0:
        return 1  # 면적이 정수이면 1을 반환
    else:
        return 0  # 면적이 정수가 아니면 0을 반환

# 입력 처리
p1, q1, p2, q2 = map(int, input().split())

# 함수 호출 및 출력
print(is_congruent(p1, q1, p2, q2))
