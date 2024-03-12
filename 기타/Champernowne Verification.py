# The
# $k^{\text{th}}$ Champernowne word is obtained by writing down the first
# $k$ positive integers and concatenating them together. For example, the
# $10^{\text{th}}$ Champernowne word is
# $12345678910$.
#
# Given a positive integer
# $n$, determine if it is a Champernowne word, and if so, which word.
#
#
# The first line contains a single integer,
# $n$ (
# $1 \le n \le 10^9$).
# $n$ will not have leading zeroes.
#
#
# If
# $n$ is the
# $k^{\text{th}}$ Champernowne word, output
# $k$. Otherwise, output
# $-1$.

n = input()
count = 0
for i in range(1, len(n)+1):
    if int(n[i-1:i]) == i: count += 1

print(count) if count == len(n) else print(-1)
