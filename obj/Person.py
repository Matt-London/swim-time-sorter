# Why is this OOP?
class Person(object):
    def __init__(self, line):
        self.name = line[0]
        self.gender = line[1]
        self.age = int(line[2])
        self.fly = line[3]
        self.back = line[4]
        self.breast = line[5]
        self.free = line[6]