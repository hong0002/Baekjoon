# 입력 받기
n, m = map(int, input().split())

# 원본 이미지 입력 받기
original_image = []
for _ in range(n):
    original_image.append(input().strip())

# 빈 줄 건너 뛰기
input()

# 네거티브 이미지 입력 받기
negative_image = []
for _ in range(n):
    negative_image.append(input().strip())

# 잘못된 픽셀 수 세기
error_count = 0
for i in range(n):
    for j in range(m):
        if original_image[i][j] == 'B' and negative_image[i][j] != 'W':
            error_count += 1
        elif original_image[i][j] == 'W' and negative_image[i][j] != 'B':
            error_count += 1

# 결과 출력
print(error_count)
