def best_setting(settings, T):
    # settings: 리스트 of 가능한 설정값 H_i
    # T: 나무의 총 높이
    best_h = None
    min_waste = T  # 초기값: worst waste = T (설정값이 T보다 크면 한 번도 못 잘려 나가므로 waste=T)
    
    for h in settings:
        waste = T % h
        if waste < min_waste:
            min_waste = waste
            best_h = h
    
    return best_h

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input().strip())
    settings = list(map(int, input().split()))
    T = int(input().strip())
    
    print(best_setting(settings, T))
