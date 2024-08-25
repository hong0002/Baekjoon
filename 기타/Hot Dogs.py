import sys

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    i = 0
    results = []
    
    while i < len(data):
        H = int(data[i])
        P = int(data[i+1])
        i += 2
        
        # Calculate the average
        average = H / P
        
        # Prepare formatted result
        formatted_average = f"{average:.2f}"
        
        # Collect the result
        results.append(formatted_average)
    
    # Output all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
