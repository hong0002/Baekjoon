import sys
input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])  # Number of rounds
    A_wins = 0
    B_wins = 0
    
    index = 1
    for _ in range(N):
        Ai = int(data[index])
        Bi = int(data[index + 1])
        if Ai > Bi:
            A_wins += 1
        elif Bi > Ai:
            B_wins += 1
        index += 2
    
    print(A_wins, B_wins)

if __name__ == "__main__":
    main()
