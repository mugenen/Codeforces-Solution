import sys
import collections

s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

c = 1

cur = s[0]
for ins in t:
    if ins == cur:
        cur = s[c]
        c += 1

print c
