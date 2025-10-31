import sys

def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    out_lines = []
    for tc in range(1, T + 1):
        N, Q = map(int, input().split())
        A = list(map(int, input().split()))
        
        # 1) 모든 부분배열 합 생성 (O(N^2))
        subsums = []
        for i in range(N):
            s = 0
            ai = A[i:]
            for x in ai:
                s += x
                subsums.append(s)
        
        # 2) 정렬
        subsums.sort()
        
        # 3) 누적합 (1-based 인덱스 대응을 위해 앞에 0 추가)
        pref = [0]
        ps = 0
        for v in subsums:
            ps += v
            pref.append(ps)
        
        out_lines.append(f"Case #{tc}:")
        for _ in range(Q):
            L, R = map(int, input().split())
            # 정렬된 부분배열합의 L..R 합
            ans = pref[R] - pref[L - 1]
            out_lines.append(str(ans))
    
    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()
