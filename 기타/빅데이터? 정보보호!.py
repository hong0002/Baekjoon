# 입력 받기
N = int(input().strip())
answers = input().strip()

# 각 문자열의 등장 횟수 계산
bigdata_count = answers.count("bigdata")
security_count = answers.count("security")

# 결과 출력
if bigdata_count > security_count:
    print("bigdata?")
elif bigdata_count < security_count:
    print("security!")
else:
    print("bigdata? security!")
