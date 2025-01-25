def calculate_leaves(a, factors):
    leaves = 1  # 첫 해에는 나무에 생장점 하나만 있음
    for i in range(a):
        splitting_factor = factors[2*i]  # 각 해의 splitting factor
        pruned_branches = factors[2*i + 1]  # 각 해의 가지치기 수
        
        # 각 해마다 나뭇가지 수를 업데이트
        leaves = leaves * splitting_factor - pruned_branches
        
    return leaves

while True:
    # 입력 받기
    data = list(map(int, input().split()))
    
    if data[0] == 0:
        break  # 입력 종료
    
    a = data[0]
    factors = data[1:]
    
    # 잎의 수 계산
    leaves = calculate_leaves(a, factors)
    
    # 결과 출력
    print(leaves)
