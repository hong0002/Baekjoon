n = int(input().strip())  # 입력받은 값을 정수로 변환
print(bin(n)[2:])        # bin() 함수로 이진수 변환 후, 앞의 "0b"를 제거하여 출력
