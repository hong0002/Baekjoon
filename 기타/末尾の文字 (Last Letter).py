def generate_string(S):
    if S[-1] == 'G':
        return S[:-1]
    else:
        return S + 'G'

# 입력 받기
N = int(input())
S = input()

# 결과 출력
print(generate_string(S))
