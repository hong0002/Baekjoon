# Pokemon Go just released the Buddy update. It lets you select a Pokemon to appear alongside your trainer’s avatar on your profile screen. As you walk with your buddy, it will find candy that can be used to evolve the Pokemon.
#
# The Buddy system divides the Pokemons into 3 groups. Each group gives one candy upon walking for 1, 3, and 5 kilometers respectively
#
# In this problem you will be given the Pokemon group G, the number of candies C you initially have, and the number of candies E required to evolve the Pokemon. You should calculate the number of Kilometers required to walk in order to evolve the Pokemon.
#
#
# Your program will be tested on one or more test cases. The first line of the input will be a single integer T, the number of test cases (1 ≤ T ≤ 100).
#
# Each test case consists of a line containing three space separated integers:
#
# G: The group of the Pokemon (1 ≤ G ≤ 3)
# C: The initial candies you have (0 ≤ C ≤ 100)
# E: The candies required to evolve the Pokemon (1 ≤ E ≤ 100)
#
#
# For each test case, print a single line containing the number of Kilometers of walking required to Evolve the Pokemon.

t = int(input())
for _ in range(t):
    g, c, e = map(int, input().split())
    if e - c <= 0:
        print(0)
    elif g == 1:
        print(e - c)
    elif g == 2:
        print(3 * (e - c))
    else:
        print(5 * (e - c))
