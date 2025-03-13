t = int(input())
for v in range(t):
    gan = [i for i in map(int, (input().split(" ")))]
    sa = [i for i in map(int, (input().split(" ")))]
    win = gan[0] + gan[1]*2 + gan[2]*3 + gan[3]*3 + gan[4]*4 + gan[5]*10
    win -= sa[0] + sa[1]*2 + sa[2]*2 + sa[3]*2 + sa[4]*3 + sa[5]*5 + sa[6]*10
    if win == 0: print(f"Battle {v+1}: No victor on this battle field")
    elif win > 0: print(f"Battle {v+1}: Good triumphs over Evil")
    else: print(f"Battle {v+1}: Evil eradicates all trace of Good")
