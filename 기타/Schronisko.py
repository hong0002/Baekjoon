# 함수: 주어진 테스트 케이스에 대해 최대 숙박 가능한 관광객 수를 계산합니다.
def max_tourists(W, K):
    # 최대 관광객 수는 각 차원의 크기를 곱한 후 2로 나눈 값입니다. (각 관광객은 2개의 칸을 차지합니다)
    return (W * K) // 2

# 주 프로그램 함수
def main():
    # 테스트 케이스 수 입력
    Z = int(input())

    # 각 테스트 케이스에 대해 반복
    for _ in range(Z):
        # 방의 크기 입력
        W, K = map(int, input().split())

        # 최대 관광객 수 계산 및 출력
        result = max_tourists(W, K)
        print(result)

# 메인 함수 호출
main()
