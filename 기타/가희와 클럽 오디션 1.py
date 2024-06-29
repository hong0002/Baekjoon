def calculate_score(level, judgement):
    # Determine the base score based on judgement and level
    if judgement == "miss":
        return 0
    elif judgement == "bad":
        return 200 * level
    elif judgement == "cool":
        return 400 * level
    elif judgement == "great":
        return 600 * level
    elif judgement.startswith("perfect"):
        # Extract the number of consecutive perfects
        if len(judgement) == 7:  # "perfect" case
            n = 1
        else:  # "perfect n연팩" case
            n = int(judgement.split()[1])
        return n * level * 1000

def main():
    # Read input
    input_line = input().strip().split()
    level = int(input_line[0])
    judgement = input_line[1]

    # Calculate the score
    score = calculate_score(level, judgement)

    # Output the result
    print(score)

if __name__ == "__main__":
    main()
