def max_snooker_score(balls):
    # 공의 점수 매핑
    values = {
        'red':    1,
        'yellow': 2,
        'green':  3,
        'brown':  4,
        'blue':   5,
        'pink':   6,
        'black':  7,
    }

    R = 0                # 남아 있는 빨간 공 개수
    cols = []            # 남아 있는 색깔 공들의 점수 리스트

    for color in balls:
        if color == 'red':
            R += 1
        else:
            cols.append(values[color])

    C = len(cols)        # 색깔 공 종류 수
    sumCol = sum(cols)   # 색깔 공 점수 합
    
    if R == 0:           # 빨간 공이 없으면 색깔 공만 한 번씩
        return sumCol
    if C == 0:           # 색깔 공이 없으면 빨간 공 하나만
        return 1

    maxCol = max(cols)   # 가장 높은 점수의 색깔 공

    # 빨간 공(R)마다 (1 + maxCol) 점, 마지막에 sumCol 점
    return R * (1 + maxCol) + sumCol


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    N = int(input())
    balls = [input().strip() for _ in range(N)]
    print(max_snooker_score(balls))
