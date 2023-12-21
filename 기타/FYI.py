def route_to_operator(phone_number):
    # 7자리 전화번호를 문자열로 변환
    phone_str = str(phone_number)
    
    # 접두사(prefix)가 "555"인지 여부를 확인
    if phone_str[:3] == "555":
        return "YES"
    else:
        return "NO"

# 입력 받기
phone_number = int(input())

# 결과 출력
result = route_to_operator(phone_number)
print(result)
