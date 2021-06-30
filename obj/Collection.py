import csv

from .Person import Person

class Collection(object):
    def __init__(self, path):
        self.people = []
        self.group = []

        self.sortedBy = -1
        
        self.build_collection(path)
    
    # Build collection from csv
    def build_collection(self, path):
        f = open(path, "r")
        csvArr = csv.reader(f, delimiter=',')

        data = []
        for line in csvArr:
            data.append(line)

        data.pop(0)

        for line in data:
            self.people.append(Person(line))

        f.close()

    # Adds a person to the list
    def append_person(self, person):
        self.people.append(person)
    
    # Gets people within age range
    def get_group(self, group, gender):
        self.group = []
        # Get age range sorted
        group = group.split(" ")
        if group[0] == -1:
            group[0] = 0
        elif group[1] == -1:
            group[1] = 100
        
        group[0] = int(group[0])
        group[1] = int(group[1])

        for person in self.people:
            person.age = int(person.age)
            if person.age >= group[0] and person.age <= group[1] and person.gender == gender:
                self.group.append(person)
        

    """
    fly - 0
    back - 1
    breast - 2
    free - 3
    """
    # Sorts by given stroke
    def sort_stroke(self, stroke):
        # Make sure everyone has a time
        for person in self.group:
            if person.fly == "":
                person.fly = 1000
            person.fly = float(person.fly)

            if person.back == "":
                person.back = 1000
            person.back = float(person.back)

            if person.breast == "":
                person.breast = 1000
            person.breast = float(person.breast)

            if person.free == "":
                person.free = 1000
            person.free = float(person.free)

        # Credit to https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
        if stroke == 0:
            self.group.sort(key=lambda x: x.fly)
        elif stroke == 1:
            self.group.sort(key=lambda x: x.back)
        elif stroke == 2:
            self.group.sort(key=lambda x: x.breast)
        elif stroke == 3:
            self.group.sort(key=lambda x: x.free)
        
        self.sortedBy = stroke
    
    def export(self, name):
        f = open("output/{}.csv".format(name), "a+")
        if self.sortedBy == 0:
            f.write(",,,BUTTERFLY,,,\n")
        elif self.sortedBy == 1:
            f.write(",,,BACKSTROKE,,,\n")
        elif self.sortedBy == 2:
            f.write(",,,BREASTSTROKE,,,\n")
        elif self.sortedBy == 3:
            f.write(",,,FREESTYLE,,,\n")

        f.write("Name,Gender,Age,Butterfly,Backstroke,Breastroke,Freestyle\n")
        for person in self.group:
            f.write("{},{},{},{},{},{},{}\n".format(person.name, person.gender, person.age, person.fly, person.back, person.breast, person.free))
        
        f.write(",,,,,,\n,,,,,,\n")
        f.close()