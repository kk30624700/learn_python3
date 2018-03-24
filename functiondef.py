"""
Show function definition
"""
#!/usr/bin/python3
#coding: utf-8

def printinfo1(str):
    print(str)
    return

def printinfo2(name, age):
    print("name: {}\tage: {}".format(name, age))
    return

def printinfo3(age, name="M24"):
    print("namee: {}\tage: {}".format(name, age))
    return 

def printinfo4(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)

sum = lambda arg1, arg2: arg1 + arg2
printinfo1("no.1")
printinfo2(name="no.1", age=28)
printinfo3(14)
printinfo4(1, 2, 3, 4)
print(sum(1, 2))