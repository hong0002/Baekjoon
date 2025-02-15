import sys

def main():
    input = sys.stdin.read  # 입력을 한번에 처리하기 위해 sys.stdin.read를 사용
    data = input().splitlines()  # 모든 입력을 줄 단위로 나누어 리스트로 받음
    
    N = int(data[0])  # 첫 번째 줄은 게임 횟수 N
    mari_score = 0
    mari_games = 0
    juri_score = 0
    juri_games = 0
    
    # 1부터 N까지 각 게임 데이터 처리
    for line in data[1:N+1]:
        player, score = line.split()
        score = int(score)
        
        if player == 'M':
            mari_score += score
            mari_games += 1
        else:  # player == 'J'
            juri_score += score
            juri_games += 1
    
    # 평균 점수 계산
    if mari_games > 0:
        mari_avg = mari_score / mari_games
    else:
        mari_avg = 0
    
    if juri_games > 0:
        juri_avg = juri_score / juri_games
    else:
        juri_avg = 0
    
    # 결과 출력
    if mari_avg > juri_avg:
        print("M")
    elif juri_avg > mari_avg:
        print("J")
    else:
        print("V")

# 실행
main()
