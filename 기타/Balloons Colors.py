def check_assignment(N, X, Y, colors):
    # Get the color of the easiest and hardest problems
    color_easy = colors[0]
    color_hard = colors[-1]
    
    # Initialize the flags
    is_easy_wrong = color_easy == X
    is_hard_wrong = color_hard == Y
    
    # Determine and return the output based on conditions
    if is_easy_wrong and is_hard_wrong:
        return "BOTH"
    elif is_easy_wrong:
        return "EASY"
    elif is_hard_wrong:
        return "HARD"
    else:
        return "OKAY"

def process_input():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        X = int(data[index + 1])
        Y = int(data[index + 2])
        index += 3
        colors = list(map(int, data[index:index + N]))
        index += N
        
        result = check_assignment(N, X, Y, colors)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    process_input()
