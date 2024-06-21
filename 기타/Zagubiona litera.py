def find_missing_letter(letters):
    import string
    
    # 전체 알파벳 집합
    all_letters = set(string.ascii_uppercase)
    
    # 입력된 25개의 알파벳 집합
    given_letters = set(letters)
    
    # 전체 알파벳에서 입력된 알파벳을 뺀 차집합
    missing_letter = all_letters - given_letters
    
    # 남은 하나의 알파벳을 반환
    return missing_letter.pop()

# 입력 받기
input_letters = input().strip()

# 결과 출력
print(find_missing_letter(input_letters))
