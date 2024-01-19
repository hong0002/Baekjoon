def decrypt_message(encrypted_str):
    decrypted_str = encrypted_str[0]  # 첫 번째 문자는 그대로 가져오기

    # 나머지 문자들을 처리
    index = 0
    while index < len(encrypted_str) - 1:
        offset = ord(encrypted_str[index]) - ord('A') + 1  # 'A'부터의 오프셋 계산
        index += offset  # 다음 문자로 이동
        decrypted_str += encrypted_str[index]  # 해당 위치의 문자를 결과 문자열에 추가

    return decrypted_str

# 입력 받기
encrypted_message = input()

# 복호화 후 출력
decrypted_message = decrypt_message(encrypted_message)
print(decrypted_message)
