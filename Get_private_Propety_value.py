## To access a private property, you can create a getter method:

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private property
        
    def get_age(self):
        return self.__age
    
p1 = Person("Sky", 43)
print(p1.get_age())