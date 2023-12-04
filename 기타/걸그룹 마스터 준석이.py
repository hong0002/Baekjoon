# 정우는 소문난 걸그룹 덕후이다. 정우의 친구 준석이도 걸그룹을 좋아하지만 이름을 잘 외우지 못한다는 문제가 있었다. 정우는 친구를 위해 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 퀴즈 프로그램을 만들고자 한다.
#
#
# 첫 번째 줄에는 총 입력 받을 걸그룹의 수 N(0 < N < 100)과 맞혀야 할 문제의 수 M(0 < M < 100)을 입력받는다.
#
# 두 번째 줄부터는 각 걸그룹마다 팀의 이름, 걸그룹의 인원 수, 멤버의 이름을 한 줄씩 차례대로 입력받는다. 팀과 멤버의 이름은 최대 100글자이며, 모든 글자는 알파벳 소문자이다. 하나의 걸그룹이나 서로 다른 두 걸그룹에 이름이 같은 두 멤버가 있는 경우는 없다.
#
# 그 다음 줄부터는 M개의 퀴즈를 입력받는다. 각각의 퀴즈는 두 줄로 이루어져 있으며, 팀의 이름이나 멤버의 이름이 첫 줄에 주어지고 퀴즈의 종류를 나타내는 0 또는 1이 두 번째 줄에 주어진다. 퀴즈의 종류가 0일 경우 팀의 이름이 주어지며, 1일 경우 멤버의 이름이 주어진다.
#
#
# 첫 번째 줄부터 차례대로 퀴즈에 대한 답을 출력한다. 퀴즈의 종류가 0일 경우 해당 팀에 속한 멤버의 이름을 사전순으로 한 줄에 한 명씩 출력한다. 퀴즈의 종류가 1일 경우 해당 멤버가 속한 팀의 이름을 출력한다.

n, m = map(int, input().split())

group_list = dict()
# 걸그룹 입력
for _ in range(n):
    group_name = input()
    head_count = int(input())
    names = []
    for _ in range(head_count):
        name = input()
        names.append(name)
    names = sorted(names)
    group_list[group_name] = names

# 퀴즈
for _ in range(m):
    quiz = input()
    op = int(input())
    flag = False
    # 맴버 이름 출력
    if op == 0:
        for i in group_list[quiz]:
            print(i)
    # 그룹명 출력
    elif op == 1:
        for i in group_list:
            for j in group_list[i]:
                if j == quiz:
                    flag = True
                    break
            # 맴버이름을 찾았다면
            if flag:
                print(i)
                break
