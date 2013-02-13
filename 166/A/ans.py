import sys
import collections

n = int(raw_input())

for i in xrange(n + 1, 100001):
    a = set(str(i))
    if len(a) == 4:
        print i
        break

