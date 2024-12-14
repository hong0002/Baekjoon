# 입력 받기
Q = int(input())  # 소리의 개수
for _ in range(Q):
    S = input().strip()  # 각 소리 문자열
    
    # "WOW" 부분 문자열 개수 세기
    count = 0
    for i in range(len(S) - 2):
        if S[i:i+3] == "WOW":
            count += 1
            
    # 결과 출력
    print(count)
