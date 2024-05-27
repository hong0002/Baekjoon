def check_padaeng_happiness(T, N, F):
    # 사탕 맛 시간의 합을 계산
    total_time = sum(F)
    
    # 파댕이가 울지 않게 만들 수 있는지 확인
    if total_time >= T:
        return "Padaeng_i Happy"
    else:
        return "Padaeng_i Cry"

# 입력값 받기
T = int(input())
N = int(input())
F = list(map(int, input().split()))

# 결과 출력
print(check_padaeng_happiness(T, N, F))
