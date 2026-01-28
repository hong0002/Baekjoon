import sys

def shift_word(a: str, b: str, c: str) -> str:
    res = []
    for x, y, z in zip(a, b, c):
        shift = (ord(y) - ord(x)) % 26
        nz = (ord(z) - ord('a') + shift) % 26
        res.append(chr(nz + ord('a')))
    return ''.join(res)

def main():
    out_lines = []
    for line in sys.stdin:
        line = line.strip()
        if line == '#':
            break
        w1, w2, w3 = line.split()
        w4 = shift_word(w1, w2, w3)
        out_lines.append(f"{w1} {w2} {w3} {w4}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
