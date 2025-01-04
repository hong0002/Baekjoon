from collections import Counter

def check_string(s):
    # 문자열의 각 문자의 출현 횟수를 셈
    count = Counter(s)
    
    # 짝수인지 홀수인지 체크할 변수
    all_even = True
    all_odd = True
    
    # 각 문자의 출현 횟수 확인
    for frequency in count.values():
        if frequency % 2 == 0:
            all_odd = False  # 짝수일 경우, all_odd는 False
        else:
            all_even = False  # 홀수일 경우, all_even은 False
    
    # 결과에 따라 출력
    if all_even:
        return 0
    elif all_odd:
        return 1
    else:
        return 2

# 입력 받기
s = input().strip()

# 함수 호출 및 결과 출력
print(check_string(s))
