import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    dice = list(map(int, input().split()))
    
    pos = 0
    score = 0
    idx = 0  # 현재 사용할 주사위 인덱스 (0~5 반복)
    
    while pos < N:
        d = dice[idx]
        idx = (idx + 1) % 6
        
        if pos + d <= N:
            pos += d
            score += pos
    
    print(score)
