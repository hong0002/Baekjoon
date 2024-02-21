# The PLU football coach must submit to the NCAA officials the names of all players that will be competing in NCAA Division II championship game. Unfortunately his computer keyboard malfunctioned and interchanged the letters ‘i’ and ‘e’. Your job is to write a program that will read all the names and print the names with the correct spelling.
#
#
# The file contains a list of names, and each name will be on a separate line.
#
#
# Print the same list of names with every ‘i’ replaced with an ‘e’, every ‘e’ replaced with an ‘i’, every ‘I’ replaced with an ‘E’, and every ‘E’ replaced with an ‘I’.

while True:
    try:
        name = list(input())
        for i, v in enumerate(name):
            if v == 'i':
                name[i] = 'e'
            elif v == 'e':
                name[i] = 'i'
            elif v == 'I':
                name[i] = 'E'
            elif v == 'E':
                name[i] = 'I'
        print(''.join(name))
    except:
        break
