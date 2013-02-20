import sys
import collections
import bisect

n, k = map(int, sys.stdin.readline().split())
seq = map(int, sys.stdin.readline().split())

seq.append(-1)
seq.sort()

L = len(seq)
cur = L - 1
size = 1

while True:
    value = seq[cur]
    if value == -1:
        break
    idx = bisect.bisect_right(seq, value / k) - 1
    found = seq[idx]
    if value % k == 0 and found == value / k:
        size += cur - idx - 1
        cur= idx - 1
    elif found == -1:
        size += cur - idx - 1
        cur = idx
    else:
        size += cur - idx
        cur = idx

print size