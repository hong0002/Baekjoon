def solve():
    import sys
    input = sys.stdin.readline
    t = int(input().strip())
    
    # 각 테스트 케이스 처리
    for _ in range(t):
        code = input().strip()  # 네 자리 코드, 예: "2843"
        # 앞의 2자리와 뒤의 2자리 숫자를 정수로 변환
        first_part = int(code[:2])
        second_part = int(code[2:])
        
        # 제곱의 합을 계산하고 7로 나눈 나머지 계산
        if (first_part**2 + second_part**2) % 7 == 1:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

# 직접 실행할 경우
if __name__ == '__main__':
    solve()
