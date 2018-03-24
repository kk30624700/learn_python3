"""
Show how to use exception
or we can use preclean like this:
with open('file') as f:
    do sth
"""
#!/usr/bin/python3
#coding: utf-8

import sys

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    f = open('/tmp/python3_file_test')
    s = f.readline()
    i = int(s.strip())
except OSError as oerr:
    print("OS Error: {0}".format(oerr))
# except ValueError as verr:
#     print("Value Error: {}".format(verr))
except:
    print("Unexpected error: ", sys.exc_info())
    raise MyError(sys.exc_info())
finally:
    f.close()

