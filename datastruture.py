"""
python datastruture
"""
#!/usr/bin/python3
#coding: utf-8

from collections import deque

stack = [3, 4, 5]
print(stack)
stack.append(6)
print(stack)
print(stack.pop())
print(stack)

queue = deque(['Eric', 'John', 'Michael'])
print(queue)
queue.append('Terry')
print(queue)
print(queue.popleft())
print(queue)

vec = [1, 2, 3]
print([3*x for x in vec])
print([(x, x**2) for x in vec])
print([3*x for x in vec if x%2!=0])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
print([[row[i] for row in matrix] for i in range(4)])

a = [1, 2, 4, 5, 6, 7, 8, 9, 0]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

t = (1, 2, 4)
print(t)

s = {1, 2, 4}
print(s)
print(1 in s)

d = {1:'a', 2:'b', 3:'c'}
print(d)
for k,v in d.items():
    print(k, v)

for i,v in enumerate(['a', 'b', 'c']):
    print(i, v)