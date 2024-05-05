def check_same_characters(N, S):
    # 문자열 S에서 첫 번째 문자를 기준으로 모든 문자와 비교하여 같은지 확인
    for char in S[1:]:
        if char != S[0]:
            return "No"
    return "Yes"

# 입력 받기
N = int(input())
S = input()

# 결과 출력
print(check_same_characters(N, S))
