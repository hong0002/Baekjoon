def MenOfPassion(n):
    # 코드1의 수행 횟수는 n과 동일합니다.
    count = n
    
    # 코드1의 수행 횟수를 다항식으로 나타내기 위해 최고차항 차수를 계산합니다.
    degree = 1  # 최고차항의 차수는 1입니다.
    
    # 최고차항의 차수가 3을 초과하는지 확인합니다.
    if degree > 3:
        degree = 4  # 최고차항의 차수가 3을 초과하면 4로 설정합니다.
    
    return count, degree

# 입력 받기
n = int(input())

# MenOfPassion 알고리즘 호출
count, degree = MenOfPassion(n)

# 결과 출력
print(count)
print(degree)
