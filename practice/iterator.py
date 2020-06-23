# Python Iterators
# https://www.w3schools.com/python/python_iterators.asp

# Iterator vs Iterable

# Return an Iterator from a tuple and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even string are iterable object, and can return an iterator:

mystr = "banana"
myitstr = iter(mystr)

print(next(myitstr))
print(next(myitstr))
print(next(myitstr))
print(next(myitstr))
print(next(myitstr))
print(next(myitstr))

# Create an Iterator
class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self

    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    # Stop after 20 iterations:
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
    


myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))