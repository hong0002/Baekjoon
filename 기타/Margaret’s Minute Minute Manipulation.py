import sys

def read_matrix(lines):
    mat = []
    for _ in range(4):
        mat.append(list(map(int, next(lines).split())))
    return mat  # 4x6

def decode(mat):
    digits = []
    for c in range(6):
        v = 0
        for r in range(4):
            v = v * 2 + mat[r][c]  # MSB가 위에 있으므로 위->아래로 이진수 구성
        digits.append(v)
    h = digits[0] * 10 + digits[1]
    m = digits[2] * 10 + digits[3]
    s = digits[4] * 10 + digits[5]
    return h * 3600 + m * 60 + s

def encode(total_seconds):
    total_seconds %= 86400
    h = total_seconds // 3600
    total_seconds %= 3600
    m = total_seconds // 60
    s = total_seconds % 60

    hhmmss = f"{h:02d}{m:02d}{s:02d}"  # 6자리
    digits = list(map(int, hhmmss))

    out = [[0]*6 for _ in range(4)]
    for c, d in enumerate(digits):
        # 위->아래 = 8,4,2,1
        out[0][c] = 1 if (d & 8) else 0
        out[1][c] = 1 if (d & 4) else 0
        out[2][c] = 1 if (d & 2) else 0
        out[3][c] = 1 if (d & 1) else 0
    return out

def main():
    lines = iter(sys.stdin.read().strip().splitlines())
    T_mat = read_matrix(lines)
    D_mat = read_matrix(lines)

    t_sec = decode(T_mat)
    d_sec = decode(D_mat)

    res_mat = encode(t_sec + d_sec)

    for r in range(4):
        print(" ".join(map(str, res_mat[r])))

if __name__ == "__main__":
    main()
