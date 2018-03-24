"""
Show the use of loop controller
"""
#!/usr/bin/python3
#coding:utf-8

loop,sum,count = 10000,0,0
while count < loop:
    sum += count
    count += 1
print(sum)