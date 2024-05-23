# 입력 받기
x, y, z = map(int, input().split())
x_prime, y_prime, z_prime = map(int, input().split())

# 학점을 결정하기 위한 조건 검사
if x_prime == x and y_prime == y and z_prime == z:
    print("A")
elif y_prime == y and z_prime == z and x_prime >= x / 2:
    print("B")
elif y_prime == y and z_prime == z:
    print("C")
elif z_prime == z and y_prime >= y / 2:
    print("D")
else:
    print("E")
