def bin_to_oct(bin_num):
    # 2진수의 길이가 3의 배수가 되도록 앞에 0을 추가
    length = len(bin_num)
    if length % 3 != 0:
        # 3의 배수로 맞추기 위해 필요한 0의 개수
        add_zeros = 3 - (length % 3)
        bin_num = '0' * add_zeros + bin_num
    
    # 3자리씩 끊어서 8진수로 변환
    oct_num = ''
    for i in range(0, len(bin_num), 3):
        # 3자리씩 자른 2진수를 8진수로 변환
        oct_num += str(int(bin_num[i:i+3], 2))
    
    return oct_num

# 입력
bin_num = input().strip()

# 출력
print(bin_to_oct(bin_num))
