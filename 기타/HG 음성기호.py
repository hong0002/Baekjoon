import sys
input = sys.stdin.readline

# 1) HG 표준음성기호 사전 정의
mapping = {
    'a': "aespa",
    'b': "baekjoon",
    'c': "cau",
    'd': "debug",
    'e': "edge",
    'f': "firefox",
    'g': "golang",
    'h': "haegang",
    'i': "iu",
    'j': "java",
    'k': "kotlin",
    'l': "lol",
    'm': "mips",
    'n': "null",
    'o': "os",
    'p': "python",
    'q': "query",
    'r': "roka",
    's': "solvedac",
    't': "tod",
    'u': "unix",
    'v': "virus",
    'w': "whale",
    'x': "xcode",
    'y': "yahoo",
    'z': "zebra",
}

S = input().rstrip()  # 길이가 최대 8e6인 문자열
n = len(S)

i = 0
answer_chars = []

while i < n:
    c = S[i]
    # S[i]가 'a'~'z'이고, 반드시 mapping에 정의되어 있으므로 예외 처리는 불필요
    code = mapping[c]
    L = len(code)
    # 남은 길이가 코드 길이보다 짧거나, 비교 결과가 다르면 에러
    if i + L > n or S[i:i+L] != code:
        print("ERROR!")
        sys.exit(0)
    # 올바르게 매칭됐다면, 원래 문자 c를 저장하고 인덱스를 건너뛴다
    answer_chars.append(c)
    i += L

# 여기까지 왔다면 전부 올바르게 분해된 것
print("It's HG!")
print("".join(answer_chars))
