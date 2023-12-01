def calculate_reward(n, d, problems_solved):
    total_problems = sum(problems_solved)
    reward_per_problem = d / total_problems

    rewards = [int(problem * reward_per_problem) for problem in problems_solved]
    return rewards

def main():
    n, d = map(int, input().split())
    problems_solved = [int(input()) for _ in range(n)]

    rewards = calculate_reward(n, d, problems_solved)

    for reward in rewards:
        print(reward)

if __name__ == "__main__":
    main()
