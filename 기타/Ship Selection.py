# 입력 받기
T = int(input())  # 테스트 케이스 수

for _ in range(T):
    N, D = map(int, input().split())  # N: 우주선 수, D: 목표 거리
    count = 0  # 목표 지점에 도달할 수 있는 우주선의 수
    
    for _ in range(N):
        v, f, c = map(int, input().split())  # v: 속도, f: 연료량, c: 연료 소비율
        # 필요한 연료량 계산: D * c / v
        if f * v >= D * c:
            count += 1
    
    print(count)
