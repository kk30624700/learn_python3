'''
How to use re
'''
#!/usr/bin/python3
#coding: utf-8
import re

line = 'cats are smarter than dogs'

matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print("match --> matchObj.group: ", matchObj.group())
else:
    print('no match!')

matchObj = re.search(r'dogs', line, re.M|re.I)
if matchObj:
    print("search --> matchObj.group: ", matchObj.group())
else:
    print('no search')

phone = '2004-959-559 # 这是一个电话号码'
num = re.sub(r'#.*$', '', phone)
print("phone: ", num)

def double(matched):
    value = int(matched.group('value'))
    return str(value*2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('hello world wide web')
print(m)

print(m.group(0))
print(m.span(0))

print(m.group(1))
print(m.span(1))

print(m.group(2))
print(m.span(2))
