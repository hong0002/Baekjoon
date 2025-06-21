import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    N = int(next(it))
    # 1야드 = 36인치, 1제곱야드 = 36*36 = 1296 제곱인치
    YARD2 = 36 * 36

    for _ in range(N):
        I = int(next(it))
        set_area = 0
        for __ in range(I):
            S = int(next(it))
            R = int(next(it))
            set_area += S * R

        # 1, 2, 3 제곱야드에서 각각 가능한 최대 세트 수
        result = []
        for yards in (1, 2, 3):
            total_area = yards * YARD2
            result.append(str(total_area // set_area))

        print(" ".join(result))

if __name__ == "__main__":
    main()
