import sys
import collections

n = int(raw_input())

home = []
guest = []
for i in xrange(n):
    h, a = map(int, sys.stdin.readline().split())
    home.append(h)
    guest.append(a)

count = 0
for i in xrange(n):
    for j in xrange(n):
        if i == j:
            continue
        if home[i] == guest[j]:
            count += 1

print count
