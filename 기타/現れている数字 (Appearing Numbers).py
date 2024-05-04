def print_unique_sorted_numbers():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])  # the length of the sequence
    A = list(map(int, data[1:N+1]))  # the sequence of numbers
    
    unique_numbers = sorted(set(A))  # get unique numbers and sort them
    
    for number in unique_numbers:
        print(number)

if __name__ == "__main__":
    print_unique_sorted_numbers()
