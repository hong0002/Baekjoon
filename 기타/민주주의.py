def count_accepted_problems(N, M, votes):
    accepted_problems = 0

    for i in range(N):
        approval_count = votes[i].count('O')
        disapproval_count = M - approval_count

        if approval_count > disapproval_count:
            accepted_problems += 1

    return accepted_problems

# 입력 받기
N, M = map(int, input().split())  # 문제 후보의 수 N, 출제위원의 수 M
votes = [input().strip() for _ in range(N)]  # 각 문제 후보에 대한 출제위원의 의견

# 결과 출력
result = count_accepted_problems(N, M, votes)
print(result)
