# -*- coding: utf-8 -*- 

#주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.


#첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.


#주어진 수들 중 소수의 개수를 출력한다.

N = int(input())
num = list(map(int, input().split()))
count = len(num) # 소수의 개수
num = sorted(num) # 정렬

if num[0] == 1: # 1은 소수가 아님
    count -= 1

for i in range(len(num)):
    for j in range(2, num[len(num) - 1] + 1): # 2부터 마지막 수까지 검사
        if num[i] > j:
            if num[i] % j == 0:      
                count -= 1
                break

print(count)
