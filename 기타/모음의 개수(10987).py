word = input()  # 단어 입력 받기

vowels = 'aeiou'  # 모음들을 나타내는 문자열
count = 0  # 모음 개수를 저장할 변수

# 입력받은 단어를 순회하면서 모음 개수 세기
for char in word:
    if char in vowels:
        count += 1

print(count)  # 결과 출력
