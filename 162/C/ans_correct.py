import sys
import collections
import math

stone = sys.stdin.readline().strip()


left = collections.deque()
right = collections.deque()
i = 0
for s in stone:
    i += 1
    if s == 'l':
        right.appendleft(i)
    else:
        left.append(i)

for p in left:
    print p
for p in right:
    print p
