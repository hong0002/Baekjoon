def solve():
    import sys
    input = sys.stdin.readline
    
    n = int(input().strip())
    best_name = ""
    best_score = -1
    
    for _ in range(n):
        name, score = input().split()
        score = int(score)
        # 현재 참가자가 최고 점수보다 높은 경우 갱신
        if score > best_score:
            best_score = score
            best_name = name
        # 점수가 같을 경우 이름이 사전순으로 앞선 경우 갱신
        elif score == best_score and name < best_name:
            best_name = name
    
    print(best_name)

# 아래 코드는 로컬 테스트를 위한 예시입니다.
if __name__ == "__main__":
    solve()
