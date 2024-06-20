def count_solved_problems(n, m, results):
    solved_count = 0
    for i in range(n):
        for j in range(m):
            if results[i][j] == '+':
                solved_count += 1
                break
    return solved_count

# 입력 받기
n, m = map(int, input().split())
results = [input().strip() for _ in range(n)]

# 결과 출력
print(count_solved_problems(n, m, results))
