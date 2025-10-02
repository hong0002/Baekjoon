n = int(input().strip())
hippos = [input().strip() for _ in range(n)]

# 고유한 피규어 개수
unique_count = len(set(hippos))

# 아직 모으지 못한 피규어 수
print(n - unique_count)
