# JOI 상사는 직원의 근무시간을 타임 카드로 관리하고있다. 직원들은 전용 장비를 사용하여 타임 카드에 출근 시간을 기록한다. 근무를 마치고 퇴근할 때도 타임 카드에 퇴근 시간을 기록한다. 타임카드에서 사용하는 시간단위는 24 시간제를 사용한다.
#
# 보안상의 이유로 직원들의 출근 시간은 7시 이후이다. 또한, 모든 직원은 23시 이전에 퇴근한다. 직원의 퇴근 시간은 항상 출근 시간보다 늦다.
#
# 입력으로 JOI 상사의 3 명의 직원 A 씨, B 씨, C 씨의 출근 시간과 퇴근 시간이 주어 졌을 때 각 직원의 근무시간을 계산하는 프로그램을 작성하라.
#
#
# 입력은 3 행으로 구성된다.
#
# 첫 번째 줄에는 A 씨의 출근 시간과 퇴근 시간,
#
# 두 번째 줄에는 B 씨의 출근 시간과 퇴근 시간,
#
# 세 번째 줄에는 C 씨의 출근 시간과 퇴근 시간이 각각 공백으로 구분되어 있다.
#
# 시간은 각각 공백으로 구분된 3 개의 정수로 쓰여져있다.
#
# 3 개의 정수 h(7 ≦ h ≦ 22), m(0 ≦ m ≦ 59), s(0 ≦ s ≦ 59)는 h시 m 분 s 초를 나타낸다.
#
#
# 첫 번째 줄에 A 씨의 근무 시간,
#
# 두 번째 줄에 B 씨의 근무 시간,
#
# 세 번째 줄에 C 씨의 근무 시간을 출력하라.
#
# 근무 시간이 h 시간 m 분 s 초이면 h, m, s의 순으로 공백으로 분리하여 출력하라.

class TimeCard:
    def __init__(self):
        self.h = 0
        self.m = 0
        self.s = 0

    def cal_time(self, time):
        self.h = time[3]
        self.m = time[4]
        self.s = time[5]
        # 초 계산
        if self.s < time[2]:
            self.m -= 1
            self.s += 60 - time[2]
        else:
            self.s -= time[2]
        # 분 계산
        if self.m < time[1]:
            self.h -= 1
            self.m += 60 - time[1]
        else:
            self.m -= time[1]
        # 시 계산
        self.h -= time[0]

a = TimeCard()
b = TimeCard()
c = TimeCard()

a.cal_time(list(map(int, input().split())))
b.cal_time(list(map(int, input().split())))
c.cal_time(list(map(int, input().split())))

print(a.h, a.m, a.s)
print(b.h, b.m, b.s)
print(c.h, c.m, c.s)
