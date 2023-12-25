# 입력 받기
p = int(input())
q = int(input())

# 조건에 따라 색상 코드 결정
if p <= 50 and q <= 10:
    print("White")
elif q > 30:
    print("Red")
else:
    print("Yellow")
