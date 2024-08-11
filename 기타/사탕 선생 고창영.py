def can_distribute_equally(test_cases):
    results = []
    for case in test_cases:
        N, candies = case
        total_candies = sum(candies)
        
        if total_candies % N == 0:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# 입력 처리
T = int(input().strip())
test_cases = []

for _ in range(T):
    input().strip()  # 빈 줄 제거
    N = int(input().strip())
    candies = []
    for _ in range(N):
        candies.append(int(input().strip()))
    test_cases.append((N, candies))

# 결과 출력
results = can_distribute_equally(test_cases)
for result in results:
    print(result)
