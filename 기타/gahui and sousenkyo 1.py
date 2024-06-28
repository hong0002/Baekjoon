def competition_rate(votes):
    # 16위 캐릭터의 득표수를 기준으로 설정합니다.
    rank_16_votes = votes[0]
    
    # 1000표 이내로 차이가 나는 캐릭터 수를 계산합니다.
    count = 0
    for vote in votes[1:]:
        if rank_16_votes - vote <= 1000:
            count += 1
    
    return count

# 입력을 받습니다.
votes = list(map(int, input().split()))

# 결과를 계산하고 출력합니다.
print(competition_rate(votes))
