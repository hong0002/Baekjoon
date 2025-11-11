import sys

def say(cmd):
    print(cmd)
    sys.stdout.flush()
    resp = sys.stdin.readline().strip()
    return resp

# 8-step Hamiltonian path from center, never revisits center:
# E, N, W, W, S, S, E, E  (end at (1,-1))
path = [
    ("move east",  "move west"),
    ("move north", "move south"),
    ("move west",  "move east"),
    ("move west",  "move east"),
    ("move south", "move north"),
    ("move south", "move north"),
    ("move east",  "move west"),
    ("move east",  "move west"),
]

actions_done = 0
found = False
back_cmd = None  # the command to step OUT of the special cell (reverse of last move)
reenter_cmd = None  # the command to step back IN (same as the move that gave 'found')

# 1~8번 액션: 탐색
for move_cmd, rev_cmd in path:
    resp = say(move_cmd)
    actions_done += 1
    if resp == "found":
        found = True
        back_cmd = rev_cmd
        reenter_cmd = move_cmd
        break
    elif resp == "bump":
        # 이 경로에선 이론상 발생하지 않음
        # 안전하게 종료 처리(원하면 여기서 폴백 전략 구현)
        print("echo Oops")
        sys.stdout.flush()
        sys.exit(0)
    # "moved"면 계속

if found:
    # 바로 한 칸 빠져나가기(액션 k+1)
    resp = say(back_cmd)
    actions_done += 1  # now adjacent to special

    # 10번째 직전까지 echo로 시간 때우기
    while actions_done < 9:
        say("echo ...")
        actions_done += 1

    # 10번째에 다시 들어가서 win
    resp = say(reenter_cmd)
    # 종료
    sys.exit(0)
else:
    # 8번 동안 found가 없었으면 특별 칸은 '중앙'
    # 현재 위치는 (1,-1).
    # 9번째: 북쪽으로 (1,0)
    resp = say("move north")
    actions_done += 1
    # 10번째: 서쪽으로 중앙 진입 → win
    resp = say("move west")
    # 종료
    sys.exit(0)
