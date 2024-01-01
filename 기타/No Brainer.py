def zombie_brains(data_sets):
    results = []

    for data_set in data_sets:
        x, y = map(int, data_set.split())
        if x >= y:
            results.append("MMM BRAINS")
        else:
            results.append("NO BRAINS")

    return results

if __name__ == "__main__":
    n = int(input())
    data_sets = [input() for _ in range(n)]

    output = zombie_brains(data_sets)

    for result in output:
        print(result)
