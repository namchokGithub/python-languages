# Python Booleans
# https://www.w3schools.com/python/python_booleans.asp

# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
 
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
# print true

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
print("\n === Functions can Return a Boolean === \n")
def myFunction():
    return True

print(myFunction())

if myFunction():
    print("Yes!!")
else:
    print("No!!")

print("=== Function isinstance ===")
x = 200
print(isinstance(x, int))