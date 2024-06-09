def calculate_1_3_sum(isbn):
    # 1-3-sum 계산을 위한 초기 값
    sum = 0
    for i in range(len(isbn)):
        if i % 2 == 0:
            sum += int(isbn[i]) * 1
        else:
            sum += int(isbn[i]) * 3
    return sum

def main():
    # 고정된 10자리 숫자
    fixed_part = "9780921418"
    
    # 사용자로부터 3자리 숫자를 입력받음
    last_digits = []
    for _ in range(3):
        last_digits.append(input())
    
    # 전체 13자리 ISBN 번호
    isbn = fixed_part + ''.join(last_digits)
    
    # 1-3-sum 계산
    result = calculate_1_3_sum(isbn)
    
    # 결과 출력
    print(f"The 1-3-sum is {result}")

if __name__ == "__main__":
    main()
