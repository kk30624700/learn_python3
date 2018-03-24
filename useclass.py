'''
How to define a class
'''
#!/usr/bin/python3
#coding: utf-8

class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("{} says: i'm {}".format(self.name, self.age))

class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("{} says: i'm {}, and i in grade {}".format(self.name, self.age, self.grade))

class speaker():
    topic = ''
    name = ''
    def __init__(self, n , t):
        self.name = n
        self.topic = t
    def speak(self):
        print("i'm {}, i am a speaker, my topic is {}".format(self.name, self.topic))

class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)
test = sample("Time", 25, 80, 4, "Python")
test.speak()
super(speaker, test).speak() # mark test as speaker, and find speaker's father as student
super(student, test).speak() # mark test as student, and find student's father as people
# super(people, test).speak()
    
