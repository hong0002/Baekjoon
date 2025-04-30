import sys
input = sys.stdin.readline

# 이기는 관계를 딕셔너리로 정의
# key가 이기는 손 모양이면 value가 지는 손 모양
win = {
    'R': 'S',  # 바위(R)는 가위(S)를 이긴다
    'S': 'P',  # 가위(S)는 보(P)를 이긴다
    'P': 'R',  # 보는 바위(R)를 이긴다
}

t = int(input())  # 테스트 케이스 수
for _ in range(t):
    n = int(input())  # 한 테스트 케이스 당 라운드 수
    p1_score = 0
    p2_score = 0

    for _ in range(n):
        a, b = input().split()
        if a == b:
            # 무승부: 아무도 점수 획득 안 함
            continue
        if win[a] == b:
            p1_score += 1
        else:
            p2_score += 1

    # 최종 승자 출력
    if p1_score > p2_score:
        print("Player 1")
    elif p2_score > p1_score:
        print("Player 2")
    else:
        print("TIE")
