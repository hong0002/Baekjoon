# 입력 받기
n = int(input().strip())

# 변수 초기화
candidate1_votes, candidate2_votes = 0, 0
candidate1_electoral, candidate2_electoral = 0, 0

# 각 주의 데이터를 처리
for _ in range(n):
    e, v1, v2 = map(int, input().split())
    
    # 총 득표 수에 더하기
    candidate1_votes += v1
    candidate2_votes += v2
    
    # 선거인단 투표 수 추가
    if v1 > v2:
        candidate1_electoral += e
    else:
        candidate2_electoral += e

# 다수 득표와 선거인단 투표 결과 비교
majority_winner = 0
electoral_winner = 0

if candidate1_votes > candidate2_votes:
    majority_winner = 1
elif candidate2_votes > candidate1_votes:
    majority_winner = 2

if candidate1_electoral > candidate2_electoral:
    electoral_winner = 1
elif candidate2_electoral > candidate1_electoral:
    electoral_winner = 2

# 최종 출력 결정
if majority_winner == 1 and electoral_winner == 1:
    print(1)
elif majority_winner == 2 and electoral_winner == 2:
    print(2)
else:
    print(0)
