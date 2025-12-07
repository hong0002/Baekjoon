import sys
input = sys.stdin.readline

def main():
    A = int(input().strip())
    a = [int(input().strip()) for _ in range(A)]
    B = int(input().strip())
    b = [int(input().strip()) for _ in range(B)]

    HALF = 12 * 60 * 2  # 1440초 (전반 끝)
    # TOTAL = 12 * 60 * 4  # 2880, 필요하면 사용

    i = j = 0
    scoreA = scoreB = 0
    first_half_points = 0

    last_leader = None  # 'A', 'B', 혹은 아직 리더 없음(None)
    turnarounds = 0

    # 두 배열을 시간 순서대로 머지
    while i < A or j < B:
        if j == B or (i < A and a[i] < b[j]):
            t = a[i]
            team = 'A'
            i += 1
        else:
            t = b[j]
            team = 'B'
            j += 1

        # 전반(1440초까지) 득점 카운트
        if t <= HALF:
            first_half_points += 1

        # 점수 갱신
        if team == 'A':
            scoreA += 1
        else:
            scoreB += 1

        # 현재 리더 판단
        if scoreA > scoreB:
            leader = 'A'
        elif scoreB > scoreA:
            leader = 'B'
        else:
            leader = '='  # 동점

        # turnaround 카운트
        if leader != '=':
            if last_leader is not None and leader != last_leader:
                # 이전에 이기고 있던 팀과 지금 이기고 있는 팀이 다르면 역전 발생
                turnarounds += 1
            # 처음 리더가 생기는 경우(last_leader is None)는 카운트하지 않음
            last_leader = leader

    print(first_half_points)
    print(turnarounds)

if __name__ == "__main__":
    main()
