import sys
import collections

n = int(sys.stdin.readline())

count = n
for i in xrange(2, n + 1):
    count -= i - 1
    count += i * (n - i + 1)
#    print i, i * (n - i + 1)

print count

"""
3
1 2 3
12 13
123
"""
