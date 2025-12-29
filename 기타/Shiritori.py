import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    
    used = set()
    first = input().strip()
    used.add(first)
    prev_last = first[-1]
    
    for i in range(2, N + 1):  # i: 현재 단어 번호(1-indexed)
        w = input().strip()
        player = 1 if i % 2 == 1 else 2  # i가 홀수면 1, 짝수면 2

        # 규칙 2: 중복 단어
        if w in used:
            print(f"Player {player} lost")
            return
        
        # 규칙 1: 이어말하기 규칙
        if w[0] != prev_last:
            print(f"Player {player} lost")
            return

        used.add(w)
        prev_last = w[-1]

    print("Fair Game")

if __name__ == "__main__":
    main()
