import sys
from collections import defaultdict

input = sys.stdin.readline

def main():
    out_lines = []
    while True:
        line = input().strip()
        if not line:
            continue
        N, M = map(int, line.split())
        if N == 0 and M == 0:
            break
        
        counts = defaultdict(int)  # player_id -> total points
        
        for _ in range(N):
            week = list(map(int, input().split()))
            for p in week:
                counts[p] += 1
        
        # 모든 선수 점수 중 1등 / 2등 점수 구하기
        scores = list(counts.values())
        max_score = max(scores)
        # 1등보다 작은 점수들 중 최댓값 = 2등 점수
        second_score = max(s for s in scores if s < max_score)
        
        # 2등 점수를 가진 선수들 모으기
        second_players = [pid for pid, sc in counts.items() if sc == second_score]
        second_players.sort()
        
        out_lines.append(' '.join(map(str, second_players)))
    
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()
