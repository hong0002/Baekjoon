def is_easy_to_pronounce(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(word) - 1):
        if (word[i] in vowels and word[i + 1] in vowels) or (word[i] not in vowels and word[i + 1] not in vowels):
            return 0
    return 1

# 입력 처리
word = input().strip()

# 결과 출력
print(is_easy_to_pronounce(word))
