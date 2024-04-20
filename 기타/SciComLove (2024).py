def reverse_string(s):
    return s[::-1]

def main():
    N = int(input())
    original_string = "SciComLove"

    if N % 2 == 0:
        print(original_string)
    else:
        reversed_string = reverse_string(original_string)
        print(reversed_string)

if __name__ == "__main__":
    main()
