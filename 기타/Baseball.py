# 테스트 케이스 수 입력 받기
T = int(input())

for _ in range(T):
    yonsei_score = 0
    korea_score = 0
    
    # 9회의 득점 입력 받기
    for _ in range(9):
        y, k = map(int, input().split())
        yonsei_score += y
        korea_score += k
    
    # 승부 판정 및 출력
    if yonsei_score > korea_score:
        print("Yonsei")
    elif korea_score > yonsei_score:
        print("Korea")
    else:
        print("Draw")
