# -*- coding: utf-8 -*- 

#단어 
#S와 정수 
#i가 주어졌을 때, 
#S의 
#i번째 글자를 출력하는 프로그램을 작성하시오.


#첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 
#S가 주어진다. 단어의 길이는 최대 
#1,000이다.

#둘째 줄에 정수 
#i가 주어진다. (
#1 \le i \le \left|S\right|)

word = input()
count = int(input())

print(word[count-1])
