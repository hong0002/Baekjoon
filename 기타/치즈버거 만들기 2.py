# BOJ 스타일 입력/출력
A, B = map(int, input().split())

# 가능성 판정: B < A <= 2B
if not (B < A <= 2 * B):
    print("NO")
else:
    K = A - B               # 버거 개수
    print("YES")
    print(K)

    # 각 버거에 치즈 1장씩 배정 후, 남은 치즈를 마지막 버거에 몰아주기
    base = [1] * K          # c_i 초기값
    R = B - K               # 남은 치즈
    if R > 0:
        base[-1] += R

    # 각 버거 문자열 출력: 'a' + 'ba' * c_i  (패티 수는 자동으로 c_i+1)
    for c in base:
        s = 'a' + 'ba' * c
        print(s)
