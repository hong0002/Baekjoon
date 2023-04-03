# -*- coding: utf-8 -*-

#무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

#1/1	1/2	1/3	1/4	1/5	…
#2/1	2/2	2/3	2/4	…	…
#3/1	3/2	3/3	…	…	…
#4/1	4/2	…	…	…	…
#5/1	…	…	…	…	…
#…	…	…	…	…	…
#이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

#X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.


#첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.


#첫째 줄에 분수를 출력한다.

x = int(input())
i = int(1)
count = int(0)

while True:
    count += i # 1 3 ...
    if x <= count:
        if i % 2 == 0: # 짝수(위에서 왼쪽으로 내려옴)
            for j in range(1, i+1):
                bj = i - j + 1 # 분자
                if count == x:
                    print(bj, "/", j, sep="")
                    break
                count -= 1 # 위치 1씩 감소(count에서 x까지 내려가며 찾기)
            break
        else: # 홀수(왼쪽에서 위로 올라감)
            count = count - i + 1 # 이전 i의 count + 1에서 x까지 올라가며 찾기
            for j in range(1, i+1):
                bj = i - j + 1 # 분자
                if count == x:
                    print(bj, "/", j, sep="")
                    break
                count += 1 # 위치 1씩 증가
            break
    i += 1
    
