import sys
import collections

n = int(raw_input())

candidate = set()
for i in xrange(3,1000):
    diff = (1-2.0/i)*180 % 1
    eps = 1e-10
    if diff <= 1e-10:
        candidate.add(int((1-2.0/i)*180 + 1e-10))

for i in xrange(n):
    a = int(raw_input())
    if a < 60:
        print 'NO'
    elif a in candidate:
        print 'YES'
    else:
        print 'NO'
