# -*- coding: utf-8 -*-

#상근이는 퀴즈쇼의 PD이다. 이 퀴즈쇼의 참가자는 총 8개 문제를 푼다. 참가자는 각 문제를 풀고, 그 문제를 풀었을 때 얻는 점수는 문제를 풀기 시작한 시간부터 경과한 시간과 난이도로 결정한다. 문제를 풀지 못한 경우에는 0점을 받는다. 참가자의 총 점수는 가장 높은 점수 5개의 합이다. 

#상근이는 잠시 여자친구와 전화 통화를 하느라 참가자의 점수를 계산하지 않고 있었다. 참가자의 8개 문제 점수가 주어졌을 때, 총 점수를 구하는 프로그램을 작성하시오.


#8개 줄에 걸쳐서 각 문제에 대한 참가자의 점수가 주어진다. 점수는 0보다 크거나 같고, 150보다 작거나 같다. 모든 문제에 대한 점수는 서로 다르다. 입력으로 주어지는 순서대로 1번 문제, 2번 문제, ... 8번 문제이다.


#첫째 줄에 참가자의 총점을 출력한다. 둘째 줄에는 어떤 문제가 최종 점수에 포함되는지를 공백으로 구분하여 출력한다. 출력은 문제 번호가 증가하는 순서이어야 한다.

score = [] # 참가자의 점수
final_score = [] # 큰 점수 5개
quiz_num = [] # 점수가 계산된 위치
[score.append(int(input())) for _ in range(8)]

final_score = sorted(score, reverse=True) # 큰 점수 순으로 정렬
final_score = final_score[:5] # 큰 점수 5개 선별

for i in final_score:
    for j in range(len(score)):
        if i == score[j]: # 점수의 위치 찾기
            quiz_num.append(j+1)

quiz_num.sort()

print(sum(final_score))
[print(i, end=" ") for i in quiz_num]
