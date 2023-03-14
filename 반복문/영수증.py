# -*- coding: utf-8 -*- 

#준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

#영수증에 적힌,

#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액
#을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.


#첫째 줄에는 영수증에 적힌 총 금액 
#X가 주어진다.

#둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
#N이 주어진다.

#이후 
#N개의 줄에는 각 물건의 가격 
#a와 개수 
#b가 공백을 사이에 두고 주어진다.


#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

total = int(input())
items_count = int(input())
sum_amount = 0

nums_matrix = [list(map(int, input().split())) for _ in range(items_count)] #2차원 리스트로 입력

for i in range(len(nums_matrix)): #입력된 가격의 합
    sum_amount += (nums_matrix[i][0] * nums_matrix[i][1])

if sum_amount == total:
    print("Yes")
else:
    print("No")
