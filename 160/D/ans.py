import sys
import collections

n = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().split())
p = int(sys.stdin.readline())

A.sort()

memo = {}

L = len(A)
for i in xrange(L):
    if A[i] <= p:
        memo[(1 << i, 1, A[i])] = 1
#print memo
def dp(bit, valid, sum):
#    print bin(bit), valid, sum
#    if sum == 0 and valid == 0:
#        print "return red:", reduce(lambda x, y:  x * y, xrange(1, bin(bit).count('1') + 1))
#        return reduce(lambda x, y:  x * y, xrange(1, bin(bit).count('1') + 1))
    if bit == 0 or sum <= 0 or valid <= 0:
        return 0
    if (bit, valid, sum) in memo:
        return memo[(bit, valid, sum)]
    
    b = bin(bit)[2:].zfill(n)
    s = 0
    L = len(b)
    for i in xrange(L):
        if b[i] == '1':
#            if sum - A[L - i - 1] <= p:
            if sum <= p:
                s += dp(bit ^ (1 << (L - i - 1)), valid - 1, sum - A[L - i - 1])
            else:
                s += dp(bit ^ (1 << (L - i - 1)), valid, sum - A[L - i - 1])
#    print "return", s, bin(bit), valid, sum
    return s


s = 0
z = n * (n + 1) / 2
for i in xrange(1, 11):
    s += dp(int('1' * n, 2), i, z) * i

denom = 1.0
for i in xrange(2, n + 1):
    denom *= i

print s / denom
