def count_failures(ops):
    """
    ops: [(연산종류, 피연산자), ...]
    연산종류는 'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE'
    """
    fail_cnt = 0

    for k in range(1, 101):
        val = k
        messed = False

        for op, x in ops:
            if op == 'ADD':
                val += x

            elif op == 'SUBTRACT':
                val -= x
                if val < 0:
                    messed = True
                    break

            elif op == 'MULTIPLY':
                val *= x

            elif op == 'DIVIDE':
                # 나누어떨어지지 않으면 분수 발생
                if val % x != 0:
                    messed = True
                    break
                val //= x

        if messed:
            fail_cnt += 1

    return fail_cnt

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    ops = []
    for _ in range(n):
        line = input().split()
        ops.append((line[0], int(line[1])))

    print(count_failures(ops))
