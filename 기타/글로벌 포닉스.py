# 세 개의 문자열 입력 받기
s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

# 각 문자열의 첫 글자 추출
first_letters = {s1[0], s2[0], s3[0]}

# 필요한 시작 글자 집합
required_letters = {'l', 'k', 'p'}

# 첫 글자들이 필요한 글자들과 정확히 일치하는지 판단
if first_letters == required_letters:
    print("GLOBAL")
else:
    print("PONIX")
