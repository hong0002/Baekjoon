import sys

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0
    results = []
    
    while True:
        N = int(data[index])
        index += 1
        
        if N == 0:
            break
        
        mary_wins = 0
        john_wins = 0
        
        for i in range(N):
            result = int(data[index + i])
            if result == 0:
                mary_wins += 1
            elif result == 1:
                john_wins += 1
        
        results.append(f"Mary won {mary_wins} times and John won {john_wins} times")
        index += N
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
