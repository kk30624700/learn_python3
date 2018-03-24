"""
Scope concept
"""
#!/usr/bin/python3
#coding: utf-8

x = int(2.9) #find int in built-in scope

g_count = 0 #scope global
def outer():
    o_count = 1 #scope enclosing 
    def inner():
        i_count = 2 #scope local