n = input()
one ="""   1
   1
   1
   1
   1"""
two = """2222
   2
2222
2
2222"""
three = """3333
   3
3333
   3
3333"""
four = """4  4
4  4
4444
   4
   4"""
five = """5555
5
5555
   5
5555"""
six = """6666
6
6666
6  6
6666"""
seven = """7777
   7
   7
   7
   7"""
eight = """8888
8  8
8888
8  8
8888"""
nine = """9999
9  9
9999
   9
   9"""
zero = """0000
0  0
0  0
0  0
0000"""

for i in n:
    if int(i) == 0: print(zero)
    elif int(i) == 1: print(one)
    elif int(i) == 2: print(two)
    elif int(i) == 3: print(three)
    elif int(i) == 4: print(four)
    elif int(i) == 5: print(five)
    elif int(i) == 6: print(six)
    elif int(i) == 7: print(seven)
    elif int(i) == 8: print(eight)
    elif int(i) == 9: print(nine)
    if i != n[-1:]: print()
