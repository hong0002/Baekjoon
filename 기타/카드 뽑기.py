def max_same_cards(N, M, K):
    # 앞면에 O가 적힌 카드와 뒷면에 O를 적을 수 있는 카드 중 최소 값을 구합니다.
    max_O = min(M, K)
    # 앞면에 X가 적힌 카드와 뒷면에 X를 적을 수 있는 카드 중 최소 값을 구합니다.
    max_X = min(N - M, N - K)
    # 두 값을 더하여 최대 개수를 구합니다.
    return max_O + max_X

# 입력을 받습니다.
N, M, K = map(int, input().split())

# 최대 개수를 계산합니다.
result = max_same_cards(N, M, K)

# 결과를 출력합니다.
print(result)
