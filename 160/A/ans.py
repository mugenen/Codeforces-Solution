import sys
import collections

n, k = map(int, sys.stdin.readline().split())
num = map(int, sys.stdin.readline().split())

c = 0
for x in num:
    s = str(x)
    if s.count('4') + s.count('7') <= k:
        c += 1
print c
