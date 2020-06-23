# Python Inheritance
# https://www.w3schools.com/python/python_inheritance.asp

class Person:
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person to create an object, and then execute the printname method:

x = Person("Namchok", "Singhachai")
x.printname()

# Create a Child Class

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)
        # or
        super().__init__(fname, lname)
        self.graduationyear =  year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

stu = Student("Mike", "Thison", 2020)
stu.welcome()


