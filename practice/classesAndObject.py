# Python Classes and Objects
# https://www.w3schools.com/python/python_classes.asp

# __init__()

###### Class name : Person #######
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

    # Should have "self"
    # def myfunc2(test):
        # print("Hello my name is " + test.name)

###### End class Person ######

p1 = Person("Jason", 38)
# print(p1.name)
# print(p1.age)
# p1.myfunc2()
p1.name = "Test name"
p1.myfunc()

del p1.age
# print(p1.age) # Error because no attribute age

# del p1 # del object

