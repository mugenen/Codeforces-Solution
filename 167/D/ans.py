import sys
import collections
import bisect
import math



n = int(raw_input())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
m = int(raw_input())


fact = [0 for i in xrange(10 ** 5 + 1)]

x = 1
for i in xrange(1, 10 ** 5 + 1):
    x *= i
    x %= m
    fact[i] = x

count = collections.Counter()

for a in A:
    count[a] += 1
for b in B:
    count[b] += 1

key = count.keys()
key.sort()

result = 1
for k in key:
    result = (result * fact[count[k]]) % m

print result
