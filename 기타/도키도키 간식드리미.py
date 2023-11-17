from collections import deque

n = int(input())
people = deque(map(int, input().split()))

my_stack = deque()
num = 1
result = []
while len(result) != n:
    if len(people) != 0:
        current = people.popleft()
        if current == num:
            result.append(current)
            num += 1
        else:
            if len(my_stack) != 0:
                if my_stack[len(my_stack)-1] == num:
                    result.append(my_stack.pop())
                    num += 1
                    people.appendleft(current) # current를 사용하지 않아서 다시 people에 넣기
                else:
                    my_stack.append(current)
            else:
                my_stack.append(current)
    else: # 줄 서있는 곳에 사람이 없으면 스택에 있는 값 모두 빼기
        result.append(my_stack.pop())

check = [i for i in range(1, n+1)]
print("Nice") if check == result else print("Sad")
