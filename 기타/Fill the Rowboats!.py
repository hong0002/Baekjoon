# Captain Jack decides to to take over a rival’s ship. He needs to send his henchmen over on rowboats that can hold 6 pirates each. You will help him count out pirates in groups of 6. The last rowboat may have fewer than 6 pirates. To make your task easier each pirate has been assigned a number from 1 to N.
#
#
# The input will be N, the number of pirates you need to send over on rowboats.
#
#
# The output will be the number of each pirate separated by spaces, with the word ”Go!” after every 6th pirate, and after the last pirate.

n = int(input())
for i in range(1, n+1):
    print(i, end=" ")
    if i % 6 == 0: print("Go!", end=" ")
if n % 6 != 0: print("Go!", end=" ")
