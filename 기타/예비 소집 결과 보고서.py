import sys
input = sys.stdin.readline

def is_diligent(times):
    # times: [T1, T2, T3], each Ti in [-1..120]
    # 푼 문제 번호들의 최대값 m 찾기
    solved = [i for i, t in enumerate(times) if t != -1]
    if not solved:
        return False
    m = max(solved)  # 0-based index: 0→1번, 1→2번, 2→3번

    # 1..m번 문제 모두 풀었는지 확인
    for i in range(m+1):
        if times[i] == -1:
            return False

    # 시간 비내림차순인지 확인
    for i in range(m):
        if times[i] > times[i+1]:
            return False

    return True

def main():
    N = int(input())
    count = 0
    for _ in range(N):
        t1, t2, t3 = map(int, input().split())
        if is_diligent([t1, t2, t3]):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
