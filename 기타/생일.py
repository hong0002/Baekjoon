# -*- coding: utf-8 -*-

#어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.


#첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)

#다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. dd mm yyyy는 생일 일, 월, 연도이다. (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.

#이름이 같거나, 생일이 같은 사람은 없다.


#첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.

nameList = []
birthList = []
n = int(input())

for i in range(n):
    name, d, m, y = input().split()
    nameList.append(name) # 이름 리스트 입력
    birthList.append(list(map(int, (d, m, y)))) # 생일 리스트 입력

maxAge = birthList[0]
minAge = birthList[0]
minIndex = 0
maxIndex = 0

# 생일 비교
for i in range(n):
    if maxAge[2] < birthList[i][2]:
        maxAge = birthList[i]
        maxIndex = i
    elif maxAge[2] == birthList[i][2]:
        if maxAge[1] < birthList[i][1]:
            maxAge = birthList[i]
            maxIndex = i
        elif maxAge[1] == birthList[i][1]:
            if maxAge[0] < birthList[i][0]:
                maxAge = birthList[i]
                maxIndex = i

    if minAge[2] > birthList[i][2]:
        minAge = birthList[i]
        minIndex = i
    elif minAge[2] == birthList[i][2]:
        if minAge[1] > birthList[i][1]:
            minAge = birthList[i]
            minIndex = i
        elif minAge[1] == birthList[i][1]:
            if minAge[0] > birthList[i][0]:
                minAge = birthList[i]
                minIndex = i

print(nameList[maxIndex], nameList[minIndex])
