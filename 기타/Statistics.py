def minimum_changes():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])  # 날 수
    p = list(map(int, data[1:]))  # 각 날의 확진자 수 리스트
    
    total_reduction = 0  # 총 감소량
    for i in range(1, n):
        if p[i] > p[i - 1]:  # 이전 날보다 현재 날이 크다면 감소 필요
            reduction = p[i] - p[i - 1]  # 감소할 양 계산
            total_reduction += reduction  # 총 감소량에 추가
            p[i] = p[i - 1]  # 현재 날의 값을 이전 날로 맞춤
    
    print(total_reduction)

# 함수 호출을 위해 주석 처리
# if __name__ == "__main__":
#     minimum_changes()
