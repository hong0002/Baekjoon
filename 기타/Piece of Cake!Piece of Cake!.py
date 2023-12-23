def calculate_largest_piece_volume(n, h, v):
    # Calculate volumes of the four pieces
    volume1 = h * v * 4
    volume2 = h * (n - v) * 4
    volume3 = (n - h) * v * 4
    volume4 = (n - h) * (n - v) * 4

    # Find the maximum volume among the four pieces
    max_volume = max(volume1, volume2, volume3, volume4)

    return max_volume

# 입력 받기
n, h, v = map(int, input().split())

# 결과 출력
result = calculate_largest_piece_volume(n, h, v)
print(result)
