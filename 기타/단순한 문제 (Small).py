def count_valid_triplets(a, b, c):
    count = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if (x % y == y % z == z % x):
                    count += 1
    return count

# 입력 받기
T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    result = count_valid_triplets(a, b, c)
    print(result)
