vote = [input() for _ in range(9)]
print("Lion") if vote.count("Lion") >= 5 else print("Tiger")
