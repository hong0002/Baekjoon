def metronome_revolutions(n):
    # 각 턴당 틱의 수
    ticks_per_turn = 4
    
    # 턴 수 계산
    revolutions = n / ticks_per_turn
    
    # 소수점 둘째 자리까지 반올림
    revolutions = round(revolutions, 2)
    
    return revolutions

# 입력 받기
n = int(input().strip())

# 결과 출력
result = metronome_revolutions(n)
print(result)
