x = int(input())  # x값 입력받기

# x가 1일 때 'U', 2일 때 'O', 0일 때 'S'를 출력
if x % 3 == 1:
    print("U")
elif x % 3 == 2:
    print("O")
else:
    print("S")
