# 달구와 포닉스는 탁구 치는 것을 좋아한다. 윤이는 오늘도 탁구를 치는 달구와 포닉스를 보고, 누가 경기에서 승리할지 예측해 보기로 했다.

# 달구와 포닉스가 탁구 경기를 진행하는 규칙은 다음과 같다. 처음에 달구와 포닉스는 점수 
# $0$점을 가지고 시작한다. 경기는 총 
# $N$회의 라운드로 구성되며 각 라운드에서 이긴 사람이 
# $1$점을 얻는다. 
# $N$회의 라운드가 모두 끝나거나, 경기 진행 도중 누군가가 
# $2$점 앞서게 되면 경기가 종료되며 이후의 라운드는 진행하지 않는다.

# 윤이는 앞으로 
# $N$회의 라운드에서 누가 이길지를 예측했다. 윤이의 예측이 맞아떨어진다면 경기가 몇 대 몇으로 끝나는지 구하시오.


# 첫 번째 줄에 경기의 수 
# $N$이 주어진다. (
# $1\le N\le 100\ 000$)

# 두 번째 줄부터 
# $N$개의 줄에 윤이가 예측한 각 라운드의 승자가 문자 하나로 주어진다. 달구가 이길 것이라면 D, 포닉스가 이길 것이라면 P가 주어진다.


# 경기가 종료된 뒤 달구와 포닉스의 점수를 각각 
# $X$와 
# $Y$라고 할 때, X:Y 형식으로 출력한다.

n = int(input())
d, p = 0, 0
for i in range(n):
    winner = input()
    if winner == 'D':
        d += 1
    elif winner == 'P':
        p += 1
    if abs(d-p) >= 2:
        break

print(d, ':', p, sep="")
