def find_kth_divisor(N, K):
    # 약수들을 저장할 리스트
    divisors = []
    
    # 1부터 N까지 돌면서 약수를 찾는다.
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    
    # 약수 리스트를 정렬한다. (이미 오름차순으로 추가되므로 정렬 생략 가능)
    divisors.sort()
    
    # K번째 약수가 존재하는지 확인하고 출력
    if K <= len(divisors):
        return divisors[K - 1]
    else:
        return 0

# 입력 받기
N, K = map(int, input().split())

# K번째 약수 출력
print(find_kth_divisor(N, K))
