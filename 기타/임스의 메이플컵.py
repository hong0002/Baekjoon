def maplecup_judge(problem_solved, union_level, max_level):
    if problem_solved >= 1000 and (union_level >= 8000 or max_level >= 260):
        return "Very Good"
    elif problem_solved >= 1000:
        return "Good"
    else:
        return "Bad"

# 입력 받기
N, U, L = map(int, input().split())

# 결과 출력
result = maplecup_judge(N, U, L)
print(result)
