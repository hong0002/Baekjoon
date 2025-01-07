def can_start_adventure(N, X, S, weapons):
    for c, p in weapons:
        if c <= X and p > S:
            return "YES"
    return "NO"


# 입력 처리
N = int(input())
X, S = map(int, input().split())
weapons = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(can_start_adventure(N, X, S, weapons))
