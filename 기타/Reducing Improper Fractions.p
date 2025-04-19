import sys

def main():
    # 첫 줄에서 테스트 케이스 수 읽기
    t = int(sys.stdin.readline().strip())
    for case in range(1, t + 1):
        line = sys.stdin.readline().strip()
        if not line:
            break
        n, d = map(int, line.split())
        # 정수 부분과 나머지 계산
        I = n // d
        r = n % d
        # 출력 문자열 구성
        if r == 0:
            # 나머지가 0이면 정수만 출력
            result = str(I)
        else:
            # 나머지가 있으면 "나머지/분모" 형태
            frac = f"{r}/{d}"
            # 정수 부분이 0이면 분수만, 아니면 "정수 분수"
            result = frac if I == 0 else f"{I} {frac}"
        print(f"Case {case}: {result}")

if __name__ == "__main__":
    main()
