import sys
import collections

import fractions


n = int(sys.stdin.readline())

expect = []
for line in sys.stdin:
    l, p = map(int, line.split())
    expect.append((l, p))

expect.sort(key = lambda x: x[1] * 10000 + x[0])

expect.reverse()

rem = 0.0

second = 0.0
for l, p in expect:
    second += rem * (100 - p) / 100
    rem += float(l) * p / 100
    second += l
#    print l, p, second, rem

#print second

#print expect

expect.sort(key = lambda x: x[0] * x[1])

expect.reverse()

rem = 0.0

second2 = 0.0
for l, p in expect:
    second2 += rem * (100 - p) / 100
    rem += float(l) * p / 100
    second2 += l
#    print l, p, second, rem

#print second2
print max(second, second2)
