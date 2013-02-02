import sys
import collections

n = int(sys.stdin.readline())

A = map(int, sys.stdin.readline().split())

last = A[-1]
count = 1
A.reverse()
for a in A[1:]:
    if a < last:
        last = a
        count += 1
    else:
        break
print len(A) - count
