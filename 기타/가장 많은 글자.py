# -*- coding: utf-8 -*-

#영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.

#어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.


#첫째 줄부터 글의 문장이 주어진다. 글은 최대 50개의 줄로 이루어져 있고, 각 줄은 최대 50개의 글자로 이루어져 있다. 각 줄에는 공백과 알파벳 소문자만 있다. 문장에 알파벳은 적어도 하나 이상 있다.


#첫째 줄에 가장 많이 나온 문자를 출력한다. 여러 개일 경우에는 알파벳 순으로 앞서는 것부터 모두 공백없이 출력한다.

import sys
input = sys.stdin.readline

alpha = [0 for _ in range(26)]

# eof 처리
text = sys.stdin.read()
text = text.replace('\n', '').replace(' ', '')

for i in text:
    alpha[ord(i) - 97] += 1

for i, v in enumerate(alpha):
    if max(alpha) == v:
        print(chr(i+97), end="")
