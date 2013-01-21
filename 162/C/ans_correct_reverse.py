import sys
import collections
import math

stone = sys.stdin.readline().strip()


left = []
right = []
i = 0
for s in stone:
    i += 1
    if s == 'l':
        right.append(i)
    else:
        left.append(i)

for p in left:
    print p
right.reverse()
for p in right:
    print p
