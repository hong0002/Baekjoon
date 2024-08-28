def count_coins(n):
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("DeadMan")
        elif i % 3 == 0:
            results.append("Dead")
        elif i % 5 == 0:
            results.append("Man")
        else:
            results.append(str(i))
    
    # Prepare the output in the required format
    output = []
    line = []
    for result in results:
        if result in ["Dead", "Man", "DeadMan"]:
            if line:
                output.append(' '.join(line))
                line = []
            output.append(result)
        else:
            line.append(result)
    if line:
        output.append(' '.join(line))
    
    return '\n'.join(output)

# Read the input
n = int(input().strip())

# Generate the output
result = count_coins(n)
print(result)
