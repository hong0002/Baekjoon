# 입력을 받아 처리하는 함수
def count_empty_bottles():
    # 테스트 케이스 개수 입력
    T = int(input())
    
    # 각 테스트 케이스에 대해 처리
    for _ in range(T):
        # E는 빈 병으로 간주하는 기준 시도 횟수, N은 병의 개수
        E, N = map(int, input().split())
        
        # 빈 병 개수를 세기 위한 변수
        empty_bottles = 0
        
        # N개의 병에 대해 각 병의 시도 횟수를 확인
        for _ in range(N):
            attempts = int(input())
            if attempts > E:
                empty_bottles += 1
        
        # 결과 출력
        print(empty_bottles)

# 함수 실행
count_empty_bottles()
