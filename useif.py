"""
This show the use of if condition
"""
#!/usr/bin/python3
#coding:utf-8
num = int(input("num: "))

if num%2 == 0:
    if num%3 == 0:
        print("num can be divided by 2 and 3")
    else:
        print("num can be divide by 2, but not 3")
elif num%3 == 0:
    print("num can be divided by 3")
else:
    print("num cannot be divided by 2 or 3")
