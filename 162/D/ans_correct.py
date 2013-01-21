import sys
import collections
import math

def divisors(n):
    temp = n
    if n <= 2:
        return
    if  temp % 2 == 0:
        while  temp % 2 ==0:
            temp /= 2
        yield 2
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if  temp % i == 0:
            while  temp % i == 0:
               temp /= i
            yield i
    if temp > 1:
        yield temp

n = int(sys.stdin.readline())
A = map(int, sys.stdin.readline().split())


length = collections.defaultdict(lambda: 0)

for n in A:
    primes = list(divisors(n))

    maximum = 0
    for p in primes:
        length[p] = max(length[p], length[p] + 1)
        maximum = max(maximum, length[p])

    for p in primes:
        length[p] = maximum

    if len(primes) == 0:
        length[n] = 1
#    print length, primes

print max(length.values())
#print list(divisors(6))