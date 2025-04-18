import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    # 학생 답안  N개 읽기
    student = [input().strip() for _ in range(N)]
    # 정답       N개 읽기
    answer  = [input().strip() for _ in range(N)]
    # 같으면 1, 다르면 0 → 합산
    correct = sum(1 for s, a in zip(student, answer) if s == a)
    print(correct)

if __name__ == "__main__":
    main()
