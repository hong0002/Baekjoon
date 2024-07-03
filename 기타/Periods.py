# 입력 읽기
n = int(input().strip())

# 각 문장을 처리
sentences = []
for _ in range(n):
    sentence = input().strip()
    if not sentence.endswith('.'):
        sentence += '.'
    sentences.append(sentence)

# 결과 출력
for sentence in sentences:
    print(sentence)
