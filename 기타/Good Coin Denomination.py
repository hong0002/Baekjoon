# 입력 받기
n = int(input())

# 각 테스트 케이스 처리
for _ in range(n):
    denominations = list(map(int, input().split()[1:]))
    
    # 출력
    print(f"Denominations: {' '.join(map(str, denominations))}")
    
    # 동전 조건 확인
    good_denominations = all(denominations[i] * 2 <= denominations[i + 1] for i in range(len(denominations) - 1))
    
    if good_denominations:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    
    print()  # 빈 줄 출력
