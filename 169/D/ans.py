import sys
import collections
import bisect

l, r = map(int, sys.stdin.readline().split())

small = bin(l)[2:]
big = bin(r)[2:]

L = len(big)
small = small.zfill(L)



for i in xrange(L):
    if small[i] != big[i]:
        print int('1' * (L - i), 2)
        break
else:
    print 0
"""
if len(small) != len(big):
    print int('1' * len(big), 2)
else:
    
"""