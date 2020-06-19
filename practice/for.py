# Python For Loops
# https://www.w3schools.com/python/python_for_loops.asp

# Example 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
for x in "banana":
    print (x)

# The break Statement
for x in fruits:
    print(x)
    if x == "banana":
        break;

for x in fruits:
    if x == "banana":
        break;
    print(x)

# Continue
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range()
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

# Else in For loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement
for x in [0, 1, 2]:
    pass