import sys
input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    # 왼쪽 위 R×C 디자인
    quarter = [list(input().rstrip()) for _ in range(R)]
    # 에러 위치 (1-indexed)
    A_err, B_err = map(int, input().split())
    
    H, W = 2*R, 2*C
    # 전체 카드 배열 초기화
    out = [[''] * W for _ in range(H)]
    
    # 1) 위쪽 절반(0 ≤ i < R) 채우기
    for i in range(R):
        for j in range(W):
            if j < C:
                # 왼쪽 위
                out[i][j] = quarter[i][j]
            else:
                # 오른쪽 위: 좌우 대칭
                out[i][j] = quarter[i][W-1-j]
    
    # 2) 아래쪽 절반(R ≤ i < 2R) 채우기: 상하 대칭
    for i in range(R):
        out[R + i] = out[R-1 - i].copy()
    
    # 3) 에러 반영 (뒤집기)
    ai, bj = A_err-1, B_err-1
    out[ai][bj] = '#' if out[ai][bj]=='.' else '.'
    
    # 4) 출력
    for row in out:
        print(''.join(row))

if __name__ == "__main__":
    solve()
