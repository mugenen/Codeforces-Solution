import sys
import collections

import fractions

memo = {}
def gcd(x, y):
    key = (x, y)
    if key in memo:
        return memo[key]
    
    memo[key] = fractions.gcd(x, y)
    return memo[key]

n = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().split())


L = len(A)

length = [1 for i in xrange(L)] 

for i in xrange(L):
    for j in xrange(0, i):
        if gcd(A[i], A[j]) != 1:
            length[i] = max(length[i], length[j] + 1)

print max(length)
