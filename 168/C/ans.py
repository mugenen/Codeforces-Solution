import sys
import collections
import bisect

n, k = map(int, sys.stdin.readline().split())
seq = map(int, sys.stdin.readline().split())

seq.sort(reverse=True)
cand = set(seq)
if k == 1:
    print len(cand)
    sys.exit(0)
for s in seq:
    if s / k <= 0:
        break
    if s not in cand:
        continue
    if s % k == 0 and s / k in cand:
        cand.remove(s / k)
print len(cand)