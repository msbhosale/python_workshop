class Person:
    first_name = "John"
    last_name = "Doe"

    def display(self):
        print(f"{self.first_name} {self.last_name}")

# Object of a Person class
john = Person()

# Calling of a method / function
john.display()

class Student:

    def __init__(self,roll_number,name):
        self.roll_number = roll_number
        self.name = name

    
    def display(self):
        print(f"{self.roll_number} {self.name} ")


pratik = Student(250,"Pratik")

# pratik.display()

print(pratik.name)

# del pratik.roll_number

# pratik.display()

pratik.roll_number = 456

pratik.display()