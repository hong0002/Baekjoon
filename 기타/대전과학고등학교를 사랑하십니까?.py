import sys

mapping = {
    "animal": "Panthera tigris",
    "tree": "Pinus densiflora",
    "flower": "Forsythia koreana",
}

out = []
for line in sys.stdin:
    q = line.strip()
    if q == "end":
        break
    out.append(mapping[q])

sys.stdout.write("\n".join(out))
