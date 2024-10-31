def find_room_distribution(n):
    # 3인용 방을 최대한 많이 사용하는 방식으로 접근
    for a3 in range(n // 3, -1, -1):
        remaining = n - (3 * a3)
        
        # 남은 인원을 2인용 방으로 배치할 수 있는지 확인
        if remaining % 2 == 0:
            a2 = remaining // 2
            return a2, a3
    
    # 불가능한 경우가 없으므로 항상 답이 존재함

# 입력 예시
n = int(input())
a2, a3 = find_room_distribution(n)

# 결과 출력
print(a2, a3)
