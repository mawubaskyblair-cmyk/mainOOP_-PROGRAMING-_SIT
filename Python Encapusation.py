### Encapsulation is about protecting data inside a class.
## Private Properties 
##1, AM you make the Properties Private by using a double underscore __ prefix.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private property
        
p1 = Person("Email", 34)
print(p1.name)
print(p1.__age) # This will cause an error because __age is private and cannot be accessed outside the class.