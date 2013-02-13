import sys
import collections
import bisect

prime = [-1] * 200000
i = 2
prime_list = []
while 200000 > i:
	if prime[i - 1] == -1:
		prime[i - 1] = 0
		temp = i * 2
		prime_list.append(i)
		while temp < 200000:
			prime[temp - 1] = 1
			temp += i
	if i == 2:
		i += 1
	else:
		i += 2



n, m = map(int, sys.stdin.readline().split())
matrix = []
for line in sys.stdin:
    matrix.append(map(int, line.split()))

diff = [[0 for i in xrange(m)] for j in xrange(n)]

m = 0
for i in xrange(100001):
    up = prime_list[bisect.bisect_left(prime_list, i)]
    m = max(m, up - i)
    if up - i == 71:
        print i, up
print m
