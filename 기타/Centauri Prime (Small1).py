def main():
    T = int(input().strip())
    vowels = set('aeiou')
    for i in range(1, T + 1):
        country = input().strip()
        last = country[-1].lower()
        if last == 'y':
            ruler = 'nobody'
        elif last in vowels:
            ruler = 'a queen'
        else:
            ruler = 'a king'
        print(f"Case #{i}: {country} is ruled by {ruler}.")

if __name__ == "__main__":
    main()
