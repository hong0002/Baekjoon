def print_j_box(size):
    if size == 1:
        print('#')
        return

    # Print the top row
    print('#' * size)
    
    # Print the middle rows
    for _ in range(size - 2):
        print('#' + 'J' * (size - 2) + '#')
    
    # Print the bottom row
    print('#' * size)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])  # Number of test cases
    sizes = list(map(int, data[1:T+1]))
    
    for i in range(T):
        print_j_box(sizes[i])
        if i < T - 1:
            print()

if __name__ == "__main__":
    main()
