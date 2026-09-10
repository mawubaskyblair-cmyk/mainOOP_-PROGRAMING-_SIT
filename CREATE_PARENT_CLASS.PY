########## Inheritance allows us to define  a class that inherits all the methods and properties from another class.#####
## Parent class is the class being inherited from , Also called base class.
## Child class is the class that inherits from another class, also called derived class.


# Creat a Parent Class
# Any class can be a parent, with Firstname and lastname properties, and a printname method.

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printnname(self):
        print(self.firstname, self.lastname)

# Use the Person create an object, and then execute the printname method.
X = Person("blair", "man")
X.printnname()
 