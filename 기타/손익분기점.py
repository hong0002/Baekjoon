# 손익분기점 계산
import sys

def main():
    A, B, C = map(int, sys.stdin.readline().split())
    
    # 가변비용 이상으로 수익을 내지 못하면
    if C <= B:
        print(-1)
        return
    
    # 손익분기점: A/(C-B)를 넘는 최소 정수
    n = A // (C - B) + 1
    print(n)

if __name__ == "__main__":
    main()
