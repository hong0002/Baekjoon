# 연도별 우승자 데이터를 사전으로 저장합니다.
winners = {
    1995: "ITMO",
    1996: "SPbSU",
    1997: "SPbSU",
    1998: "ITMO",
    1999: "ITMO",
    2000: "SPbSU",
    2001: "ITMO",
    2002: "ITMO",
    2003: "ITMO",
    2004: "ITMO",
    2005: "ITMO",
    2006: "PetrSU, ITMO",
    2007: "SPbSU",
    2008: "SPbSU",
    2009: "ITMO",
    2010: "ITMO",
    2011: "ITMO",
    2012: "ITMO",
    2013: "SPbSU",
    2014: "ITMO",
    2015: "ITMO",
    2016: "ITMO",
    2017: "ITMO",
    2018: "SPbSU",
    2019: "ITMO"
}

# 입력을 받습니다.
y = int(input().strip())

# 해당 연도의 우승자를 출력합니다.
print(winners[y])
