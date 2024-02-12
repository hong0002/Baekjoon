# 각각의 입력을 받아옴
digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())

# 조건을 확인하여 출력
if (digit1 == 8 or digit1 == 9) and (digit4 == 8 or digit4 == 9) and (digit2 == digit3):
    print("ignore")
else:
    print("answer")
