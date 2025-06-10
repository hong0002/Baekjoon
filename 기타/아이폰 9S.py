import sys
input = sys.stdin.readline

def main():
    N = int(input())
    B = [int(input()) for _ in range(N)]
    
    answer = 0
    for x in set(B):
        prev = None
        curr_len = 0
        max_len = 0
        
        for b in B:
            if b == x:
                # 용량 x인 사람은 모두 제거
                continue
            if b == prev:
                curr_len += 1
            else:
                prev = b
                curr_len = 1
            max_len = max(max_len, curr_len)
        
        answer = max(answer, max_len)
    
    print(answer)

if __name__ == "__main__":
    main()
