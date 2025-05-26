def max_score(k: int, you: str, friend: str) -> int:
    n = len(you)
    # m = 같은 위치에 같은 답을 쓴 개수
    m = sum(1 for i in range(n) if you[i] == friend[i])
    d = n - m
    # 친구가 맞춘 k문제 중 최대 m문제는 당신과 일치 위치에서, 
    # 나머지 (n-k)문제 중 최대 d문제는 불일치 위치에서 당신이 맞힐 수 있음
    return min(m, k) + min(d, n - k)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    k = int(input())
    you = input().strip()
    friend = input().strip()
    print(max_score(k, you, friend))
