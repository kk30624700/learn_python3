#!/usr/bin/python3
#coding: utf-8

import sqlite3

conn = sqlite3.connect('/tmp/python_db')
cursor = conn.cursor()

try:
    cursor.execute('create table user(id varchar(32) primary key, name varchar(20))')
    cursor.execute('insert into user(id, name) values("1", "Michael")')
    print("rowcount: {}".format(cursor.rowcount))
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()

conn = sqlite3.connect('/tmp/python_db')
cursor = conn.cursor()

try:
    cursor.execute('select * from user')
    values = cursor.fetchall()
    print(values)
except:
    conn.rollback()
finally:
    cursor.close()
    conn.close()