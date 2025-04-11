def main():
    import sys
    input = sys.stdin.readline

    # 강의실 개수 N과 예약 요청 개수 M을 입력받음
    N, M = map(int, input().split())
    
    # 각 강의실의 현재 마지막 예약 종료 시간 저장 (초기값은 모두 0)
    classroom_end = [0] * (N + 1)
    
    result = []  # 결과를 저장할 리스트

    # M개의 예약 요청을 순서대로 처리
    for _ in range(M):
        # k: 강의실 번호, s: 예약 시작 시간, e: 예약 종료 시간
        k, s, e = map(int, input().split())
        
        # 현재 강의실의 마지막 종료 시간 <= 새로운 예약의 시작 시간이면 수락
        if classroom_end[k] <= s:
            result.append("YES")
            classroom_end[k] = e  # 종료 시간 갱신
        else:
            result.append("NO")
    
    # 결과 출력
    print("\n".join(result))

if __name__ == "__main__":
    main()
