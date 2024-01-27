# 입력 받기
S, K, H = map(int, input().split())

# 참여도의 합 계산
total_participation = S + K + H

# 일처리 평가
if total_participation >= 100:
    print("OK")
else:
    # 참여도가 가장 낮은 대학 찾기
    min_participation = min(S, K, H)
    
    # 참여도가 가장 낮은 대학의 영문 이름 출력
    if min_participation == S:
        print("Soongsil")
    elif min_participation == K:
        print("Korea")
    else:
        print("Hanyang")
