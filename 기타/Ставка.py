def main():
    import sys
    input = sys.stdin.readline

    t = int(input().strip())
    results = []
    
    for _ in range(t):
        A, C = map(int, input().split())
        r, g, b = map(int, input().split())
        
        # RED를 추가했을 때의 점수
        score_red = A * ((r + 1) ** 2 + g ** 2 + b ** 2) + C * min(r + 1, g, b)
        # GREEN를 추가했을 때의 점수
        score_green = A * (r ** 2 + (g + 1) ** 2 + b ** 2) + C * min(r, g + 1, b)
        # BLUE를 추가했을 때의 점수
        score_blue = A * (r ** 2 + g ** 2 + (b + 1) ** 2) + C * min(r, g, b + 1)
        
        # 최댓값을 찾는다.
        max_score = max(score_red, score_green, score_blue)
        
        if max_score == score_red:
            results.append("RED")
        elif max_score == score_green:
            results.append("GREEN")
        else:
            results.append("BLUE")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
