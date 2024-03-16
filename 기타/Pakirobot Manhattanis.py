def min_steps_to_warehouse(N, steps):
    # Calculate net north-south and east-west movement
    net_ns = steps.count('N') - steps.count('S')
    net_ew = steps.count('E') - steps.count('W')
    
    # Minimum steps required to return to the warehouse
    return abs(net_ns) + abs(net_ew)

# 입력 받기
N = int(input())
steps = input().strip()

# 결과 출력
print(min_steps_to_warehouse(N, steps))
