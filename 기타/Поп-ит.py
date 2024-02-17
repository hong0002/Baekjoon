def min_flips_to_make_uniform(h, w, pop_it):
    # Count the number of '0's and '1's in the pop-it
    count_0 = sum(row.count('0') for row in pop_it)
    count_1 = sum(row.count('1') for row in pop_it)
    
    # Return the minimum number of flips needed to make all bubbles in the same state
    return min(count_0, count_1)

# 입력 받기
h, w = map(int, input().split())
pop_it = [input().strip() for _ in range(h)]

# 결과 출력
result = min_flips_to_make_uniform(h, w, pop_it)
print(result)
