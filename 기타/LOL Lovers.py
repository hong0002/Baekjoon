def divide_food():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 음식의 개수
    s = data[1]  # 음식 문자열
    
    for k in range(1, n):  # 1부터 n-1까지 시도
        my_items = s[:k]  # 내가 가져갈 부분
        friend_items = s[k:]  # 친구가 가져갈 부분
        
        my_L = my_items.count('L')
        my_O = my_items.count('O')
        friend_L = friend_items.count('L')
        friend_O = friend_items.count('O')
        
        # 조건을 확인
        if my_L != friend_L and my_O != friend_O:
            print(k)
            return
    
    # 조건을 만족하는 k가 없으면 -1 출력
    print(-1)

#함수 호출을 위해 주석 처리
if __name__ == "__main__":
    divide_food()
