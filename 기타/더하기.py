# 테스트 케이스의 수 T를 입력받는다.
T = int(input())

# T번 만큼 반복
for _ in range(T):
    # 자연수의 개수 N을 입력받는다. (실제로 이 N은 사용되지 않지만 입력으로 받아야 함)
    N = int(input())
    # N개의 자연수를 입력받고 합을 계산하여 출력한다.
    numbers = list(map(int, input().split()))
    print(sum(numbers))
