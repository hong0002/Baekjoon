# -*- coding: utf-8 -*-

#네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.


#첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 네 줄로 이루어져 있으며, 점의 좌표가 한 줄에 하나씩 주어진다. 점의 좌표는 -100,000보다 크거나 같고, 100,000보다 작거나 같은 정수이다. 같은 점이 두 번 이상 주어지지 않는다.


#각 테스트 케이스마다 입력으로 주어진 네 점을 이용해서 정사각형을 만들 수 있으면 1을, 없으면 0을 출력한다.

T = int(input())
list_s = []

for i in range(T):
    square = [list(map(int, input().split())) for _ in range(4)]

    for j in range(4):
        for k in range(j+1, 4):
            list_s.append(abs(square[j][0] - square[k][0])**2 + abs(square[j][1] - square[k][1])**2) # 0번 점부터 각 점까지의 길이 구하기
    list_s = sorted(list_s) # 정렬

    if list_s[0] == list_s[1] == list_s[2] == list_s[3] and list_s[4] == list_s[5]: # 네 변의 길이가 같고, 대각선의 길이가 같으면
        print(1)
    else:
        print(0)

    list_s.clear() # 리스트 초기화
