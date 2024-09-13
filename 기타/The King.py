def maximize_potential_sum():
    N = int(input())
    p = int(input())
    potentials = list(map(int, input().split()))
    max_sum = 0
    for potential in potentials:
        v_i = potential ** p
        if v_i > 0:
            max_sum += v_i
    print(max_sum)

maximize_potential_sum()
