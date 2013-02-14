import sys
import collections

memo = {}


n = int(raw_input())
stair = map(int, sys.stdin.readline().split())

m = int(raw_input())
block = []
for i in xrange(m):
    block.append(map(int, sys.stdin.readline().split()))

cur_h = stair[0]
result = []
for b in block:
    temp_h = max(cur_h, stair[b[0] - 1])
    result.append(temp_h)
    cur_h = temp_h + b[1]

for r in result:
    print r
