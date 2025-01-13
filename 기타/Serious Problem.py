def annoying_count(s):
    count_2 = s.count('2')
    count_e = s.count('e')
    if count_2 > count_e:
        return '2'
    elif count_e > count_2:
        return 'e'
    else:
        return 'yee'


# 입력 처리
_ = int(input().strip())  # 문자열 길이는 사용하지 않음
s = input().strip()

# 결과 출력
print(annoying_count(s))
