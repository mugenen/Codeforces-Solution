import sys
import collections
import bisect
import math
class Trie:
    class Node:
        def __init__(self, x, bros = None, child = None):
            self.data = x
            self.bros = bros
            self.child = child

        def get_child(self, x):
            child = self.child
            while child:
                if child.data == x: break
                child = child.bros
            return child

        def set_child(self, x):
            child = Trie.Node(x, self.child)
            self.child = child
            return child

        def traverse(self, leaf, filter, count, k):
#            print self.data
            if self.data == '$':
                yield 1
            else:
                child = self.child
                while child:
                    temp = count
                    if self.data in filter:
                        temp += 1
                        if temp > k:
                            child = child.bros
                            continue
                    for x in child.traverse(leaf, filter, temp, k):
                        yield x
                    child = child.bros
    
    def __init__(self, x = None):
        self.root = Trie.Node(None)
        self.leaf = x

    def insert(self, seq):
        node = self.root
        for x in seq:
            child = node.get_child(x)
            if not child:
                child = node.set_child(x)
            node = child
        if not node.get_child(self.leaf):
            node.set_child(self.leaf)
    
    def traverse(self, filter, k):
        node = self.root.child
        while node:
            for x in node.traverse(self.leaf, filter, 0, k):
                yield x
            node = node.bros
    
string = raw_input()
filter_txt = raw_input()
k = int(raw_input())

filter = set()

A = ord('a')
for i in xrange(len(filter_txt)):
    if filter_txt[i] == '0':
        filter.add(chr(A + i))

trie = Trie()
for i in xrange(len(string)):
    for j in xrange(i + 1, len(string) + 1):
        trie.insert(string[i:j] + '$')
#        print string[i:j] + '$', i, j

result = 0
check = set()
for s in trie.traverse(filter, k):
    result += s
#    if s != []:
#        print s
#        check.add(''.join(s))
#        result += 1
print result
#print len(check)
