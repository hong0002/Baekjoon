def zerinho_winner(A, B, C):
    if A != B and A != C:
        winner = 'A'
    elif B != A and B != C:
        winner = 'B'
    elif C != A and C != B:
        winner = 'C'
    else:
        winner = '*'
    
    return winner

# 입력 받기
A, B, C = map(int, input().split())

# 함수 호출 및 결과 출력
result = zerinho_winner(A, B, C)
print(result)
