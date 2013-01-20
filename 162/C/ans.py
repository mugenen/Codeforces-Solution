import sys
import collections
import math

stone = sys.stdin.readline().strip()

def logsumexp(x, y):
    large = max(x, y)
    small = min(x, y)
    return large + math.log(math.exp(small - large) + 1)

def logdiffexp(x, y):
    large = max(x, y)
    small = min(x, y)
    return large + math.log(- math.exp(small - large) + 1)

cur = math.log(0.1)
pos = [(cur, 1)]
step = cur

i = 2
for s in stone[:-1]:
    step -= math.log(2.0)
    if s == 'l':
        cur = logdiffexp(cur, step)
    else:
        cur = logsumexp(cur, step)
    pos.append((cur, i))
    i += 1

pos.sort()

for p in pos:
    print p[1]
