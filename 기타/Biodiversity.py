import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().strip())
species = [input().strip() for _ in range(N)]

counter = Counter(species)
most_common_species, max_count = counter.most_common(1)[0]

if max_count > N - max_count:
    print(most_common_species)
else:
    print("NONE")
