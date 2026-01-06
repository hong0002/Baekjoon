import sys
import heapq

def main():
    input = sys.stdin.buffer.readline

    K, N = map(int, input().split())

    heaps = [[] for _ in range(26)]  # heaps[i] = list of (count, word)

    # read words
    for _ in range(K):
        w = input().decode().strip()
        idx = ord(w[0]) - 97
        heaps[idx].append((0, w))

    # heapify each
    for i in range(26):
        heapq.heapify(heaps[i])

    out = []
    for _ in range(N):
        line = input()
        c = line[0]  # ascii code of the letter (e.g., b'z'[0])
        idx = c - 97

        cnt, w = heapq.heappop(heaps[idx])
        out.append(w)
        heapq.heappush(heaps[idx], (cnt + 1, w))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
