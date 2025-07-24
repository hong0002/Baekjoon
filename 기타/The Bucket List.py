import sys
import heapq

def main():
    input = sys.stdin.readline
    N = int(input())
    events = []
    
    for i in range(N):
        s, t, b = map(int, input().split())
        events.append((s, 'start', i, b))
        events.append((t, 'end',   i, 0))
    
    # 시간 순으로 정렬
    events.sort(key=lambda x: x[0])
    
    available = []      # 사용 가능한 양동이 번호들의 최소 힙
    next_label = 0      # 지금까지 발급된 최대 양동이 번호
    alloc = {}          # alloc[i] = 소 i에게 할당된 양동이 번호 리스트
    
    for time, typ, idx, need in events:
        if typ == 'start':
            alloc[idx] = []
            for _ in range(need):
                if available:
                    lbl = heapq.heappop(available)
                else:
                    next_label += 1
                    lbl = next_label
                alloc[idx].append(lbl)
        else:  # 'end'
            # 소 idx가 쓰던 양동이 반납
            for lbl in alloc[idx]:
                heapq.heappush(available, lbl)
    
    print(next_label)

if __name__ == "__main__":
    main()
