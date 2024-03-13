# The Vowels are a, e, i, o and u, and possibly y. People disagree on whether y is a vowel or not. Unfortunately for you, you have been tasked with counting the number of vowels in a word. You'll have to count how many vowels there are assuming y is a vowel, and assuming y is not.
#
#
# The single line of input contains a string of at least one and at most
# $50$ lowercase letters.
#
#
# Output two space-separated integers. The first is the number of vowels assuming y is not a vowel, the second is the number of vowels assuming y is a vowel.

letter = input()

vowels = ['a', 'e', 'i', 'o', 'u']
count, ycount = 0, 0
for i in letter:
    if i in vowels: count += 1
    elif i == 'y': ycount += 1

print(count, count+ycount)
