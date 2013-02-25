import sys
import collections

line = sys.stdin.readline().strip()

count = collections.Counter()
for c in line:
    count[c] += 1

odd = 0
even = 0
for c in count:
    if count[c] % 2 == 1:
        odd += 1
    else:
        even += 1

isFirst = True

while odd > 1:
#    print isFirst, even, odd
    if even > 0:
        even -= 1
        odd += 1
    else:
        odd -= 1
    isFirst = not isFirst
if isFirst:
    print 'First'
else:
    print 'Second'
