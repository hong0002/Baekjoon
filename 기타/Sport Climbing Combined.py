import sys

input = sys.stdin.readline

n = int(input().strip())
players = []

for _ in range(n):
    b, p, q, r = map(int, input().split())
    score = p * q * r      # 곱 점수
    sum_score = p + q + r  # 합 점수
    # 정렬 기준: (곱 점수, 합 점수, 등번호)
    players.append((score, sum_score, b))

# 기준대로 정렬
players.sort()

# 상위 3명 등번호 출력
gold = players[0][2]
silver = players[1][2]
bronze = players[2][2]

print(gold, silver, bronze)
