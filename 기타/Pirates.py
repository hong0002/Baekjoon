from collections import Counter

# 입력 받기
n = int(input().strip())  # 단어 길이 (사용하지 않음)
word = input().strip()    # 단어

# 문자 빈도 계산
frequency = Counter(word)

# 가장 많이 등장한 문자와 그 횟수 찾기
most_common_char, count = frequency.most_common(1)[0]

# 결과 출력
print(most_common_char, count)
