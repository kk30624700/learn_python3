"""
Show the use of file
"""
#!/usr/bin/python3
#coding: utf-8

f = open("/tmp/python3_file_test", 'a+')
f.write("life is short, use python\n")
f.write("life is short, use python\n")
f.write("life is short, use python\n")
f.flush();

print(f.tell())
f.seek(0)
print(f.tell())
str = f.read()
print(str)

f.seek(0)
str = f.readline()
print(str)

str = f.readlines()
print(str)

f.seek(0)
for line in f:
    print(line, end='')

f.close()