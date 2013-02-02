import sys
import collections
import bisect
import math

n = int(sys.stdin.readline())

sq = []
i = 1
while i * i <= 1e9:
    sq.append(i*i + 1e-10)
    i += 1

m = -1
for z in xrange(n):
    k, a = map(int, sys.stdin.readline().split())
    num = bisect.bisect(sq, a)
    
    cand = math.log(num + 1) + k * math.log(2)
    
    lb = 0
    ub = 1e9
    while ub - lb > 1:
        mid = int(lb + ub) / 2
        possible = mid * math.log(2)
        
        if possible >= cand:
            ub = mid
        else:
            lb = mid
        m = max(m, ub)

print m
