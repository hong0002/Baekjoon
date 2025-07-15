def count_surrounding_pairs(S: str) -> int:
    stack = []
    pairs = []
    star_pos = None

    # 1) 매칭 쌍과 별표 위치 찾기
    for i, c in enumerate(S):
        if c == '(':
            stack.append(i)
        elif c == ')':
            l = stack.pop()
            pairs.append((l, i))
        else:  # c == '*'
            star_pos = i

    # 2) 별표를 둘러싼 쌍 개수 세기
    count = 0
    for l, r in pairs:
        if l < star_pos < r:
            count += 1
    return count

if __name__ == "__main__":
    import sys
    S = sys.stdin.readline().strip()
    print(count_surrounding_pairs(S))
