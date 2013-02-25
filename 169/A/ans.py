import sys
import collections

n, k = map(int, raw_input().split())

m = -10**10
for i in xrange(n):
    f, t = map(int, raw_input().split())
    if t > k:
        m = max(m, f - (t - k))
    else:
        m = max(m, f)
print m
