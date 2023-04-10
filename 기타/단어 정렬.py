# -*- coding: utf-8 -*-

#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

#길이가 짧은 것부터
#길이가 같으면 사전 순으로
#단, 중복된 단어는 하나만 남기고 제거해야 한다.


#첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.


#조건에 따라 정렬하여 단어들을 출력한다.

import sys

n = int(input())
word = set()
word_start = 0 # 같은 길이 단어의 시작 인덱스
word_end = 0 # 같은 길이 단어의 끝 인덱스
flag1 = False
flag2 = False

[word.add(sys.stdin.readline().rstrip()) for _ in range(n)] # \n제거 후 집합에 입력

word = list(word)
word.sort(key=len) # 길이 정렬
word_len = len(word[0]) # 처음 단어의 길이

for i in range(len(word)):
    if flag1 == False and len(word[i]) == word_len:
        word_start = i
        flag1 = True
    if i < len(word) - 1: # 다음 단어가 있을 때
        if flag1 == True and len(word[i+1]) != word_len: # 다음 단어와 길이가 다르다면
            word_end = i
            word[word_start:word_end+1] = sorted(word[word_start:word_end+1])
            word_len = len(word[i+1])
            flag1 = False
            flag2 = True
else: 
    if flag2 == False: # 리스트 안의 단어의 길이가 모두 같을 때
        word = sorted(word)
    else: # 마지막 길이 단어 정렬
        word[word_start:] = sorted(word[word_start:])
    
[print(i) for i in word]
