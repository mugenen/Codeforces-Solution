import sys
import collections

n, m = map(int, sys.stdin.readline().split())

tile = [[0 for i in xrange(m)] for j in xrange(n)]

candidate = set()
for i in xrange(n):
    temp = raw_input()
    for j in xrange(m):
        if temp[j] == 'B':
            tile[i][j] = 1
            candidate.add((i, j))

check = [[0 for i in xrange(m + 2)] for j in xrange(n + 2)]

stack = [list(candidate)[0]]
visited = set()
while len(stack) > 0:
    cur = stack.pop()
    visited.add(cur)
    x, y = cur

    dir_x = [1, 0, 0, -1]
    dir_y = [0, -1, 1, 0]
    for i in xrange(4):
        key = (x + dir_x[i], y + dir_y[i])
        if key in candidate and key not in visited:
            stack.append(key)

if visited != candidate:
    print 'NO'
    sys.exit(0)

for i in xrange(n):
    start = False
    for j in xrange(m):
        if tile[i][j] == 1:
            if not start:
                start = True
            elif tile[i][j - 1] != 1:
                print 'NO'
                sys.exit(0)

for j in xrange(m):
    start = False
    for i in xrange(n):
        if tile[i][j] == 1:
            if not start:
                start = True
            elif tile[i - 1][j] != 1:
                print 'NO'
                sys.exit(0)


print 'YES'