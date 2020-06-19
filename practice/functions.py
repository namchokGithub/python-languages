# Python Functions
# https://www.w3schools.com/python/python_functions.asp

# Creating a Function
# def my_fucntion():
#     print("Hello from a function")

### Calling a Function
# my_fucntion()

### Arguments
# def my_fucntion(fname):
#     print(fname + " Refsnes")

# my_fucntion("test")
# my_fucntion("mhee")

### Number of Arguments
# def my_function(fname, lname):
#     print(fname + " " + lname)

# my_function("Email", "Refsnes")

### Arbitrary Argument, *args
# def my_function(*kids):
#     print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

### Keyword Arguments
# def my_fucntion(child3, child2, child1):
#     print("The youngest chuild is " + child3)

# my_fucntion(child1="Email", child2="Tobias", child3="Linus")

### Arbitraty Keyword Arguments, **kwargs
# def my_fucntion(**kid):
#     print("His last name is " + kid["lname"])

# my_fucntion(fname = "Tobias", lname = "Refsnes")

### Default Parameter Value
# def my_function(country = "Norway"):
#     print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()

### Passing a List as an Argument
# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

### Return Values
# def my_fucntion(x):
#     return x * 5

# print(my_fucntion(5))

### The pass Statement
# def my_fucntion():
#     pass

### Recursion
def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")

tri_recursion(6)