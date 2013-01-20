import sys
import collections

n = int(sys.stdin.readline())

trees = []
for line in sys.stdin:
    trees.append(int(line.strip()))
height = trees[0]
cost = height + 1

for t in trees[1:]:
#    print height, cost
    diff = abs(t - height)
    height = t
    cost += diff + 2

print cost
