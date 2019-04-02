class Person:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(f"{self.first_name} {self.last_name}")


class Student(Person):
    
    def __init__(self,roll_number,first_name,last_name):
        Person.__init__(self,first_name,last_name)
        self.roll_number = roll_number

s1 = Student(201,"Ajay","Patil")

s1.display()