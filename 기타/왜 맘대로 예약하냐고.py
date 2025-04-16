# 입력 받기
T, X = map(int, input().split())
N = int(input())

# 모든 조원이 X 교시에 참석 가능한지 여부 체크
all_attend = True  # 초기값 True로 설정

for _ in range(N):
    K = int(input().strip())  # 조원이 가능한 교시의 개수 (사용하지 않음)
    available_times = list(map(int, input().split()))
    
    # X가 이 조원의 가능한 교시 목록에 없는 경우
    if X not in available_times:
        all_attend = False
        break  # 한 명이라도 참석 불가하면 반복 중지

# 결과 출력
if all_attend:
    print("YES")
else:
    print("NO")
