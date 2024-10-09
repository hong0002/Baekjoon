# 첫 번째 입력: 테스트 케이스의 개수 T
T = int(input())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    # 후보자 수 N과 지역 수 M을 입력받음
    N, M = map(int, input().split())
    
    # 후보자별 득표수를 저장할 리스트 초기화
    votes = [0] * N
    
    # 각 지역의 득표수를 후보자별로 합산
    for _ in range(M):
        region_votes = list(map(int, input().split()))
        for i in range(N):
            votes[i] += region_votes[i]
    
    # 가장 많은 득표수를 얻은 후보자를 찾기
    winner = votes.index(max(votes)) + 1  # 1부터 시작하는 인덱스로 출력
    print(winner)
