import sys
import collections

push = [[0 for i in xrange(5)] for j in xrange(5)]

for i in xrange(3):
    temp = map(int, raw_input().split())
    for j in xrange(3):
        push[i + 1][j + 1] += temp[j]
        push[i][j + 1] += temp[j]
        push[i + 1][j] += temp[j]
        push[i + 2][j + 1] += temp[j]
        push[i + 1][j + 2] += temp[j]

result = []
for i in xrange(3):
    temp = ''
    for j in xrange(3):
        if push[i + 1][j + 1] % 2 == 1:
            temp += '0'
        else:
            temp += '1'
    result.append(temp)

for r in result:
    print r

