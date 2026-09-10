## use the student class to object, and then execute the printname method 

# X = Student("Sea", "Olsen")
# X.printname()
# solution.

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

class student(Person):
    pass

X = student("blair", "Sky")
X.printname()
