# 입력 받기
l1, r1, l2, r2, k = map(int, input().split())

# 겹치는 구간 계산
start = max(l1, l2)
end = min(r1, r2)

# 겹치는 구간이 없는 경우
if start > end:
    print(0)
else:
    # 겹치는 구간 길이
    overlap = end - start + 1
    
    # 전화 통화 시간 처리
    if start <= k <= end:
        overlap -= 1  # 통화 시간이 겹치는 경우 1분 제외
    
    print(max(overlap, 0))  # 음수 방지를 위해 0과 비교
