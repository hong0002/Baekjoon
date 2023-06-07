# -*- coding: utf-8 -*-

#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.


#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.


#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

flag = False
count = 0 # 가장 많이 사용된 알파벳이 여러 개 존재하는지 판단하는 변수
alpha = [0]*26
sentence = input()
sentence = sentence.upper() # 대문자 전환

for i in sentence:
    alpha[ord(i)-65] += 1 # 리스트에 A~Z 순서로 삽입

maxCount = max(alpha)
maxAlpha = 0
for i in range(len(alpha)):
    if alpha[i] == maxCount:
        maxAlpha = i
        count += 1
        if count > 1:
            print('?')
            flag = True
            break    

if flag == False:
    print(chr(maxAlpha+65))
