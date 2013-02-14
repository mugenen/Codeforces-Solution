import sys
import collections

n = int(raw_input())

hand = map(int, raw_input().split())
s = sum(hand) - 1

result = 0
for i in xrange(1, 6):
    if (s + i) % (n + 1) != 0:
#        print s, i, (s + i) % (n + 1)
        result += 1
print result
