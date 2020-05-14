# Python Tuples
# https://www.w3schools.com/python/python_tuples.asp

# Example
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("=== Access Tuple Items ===")

print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "kiwi", "mango", "melon")

# Range of Indexes
print(thistuple[2:4])
# Range of Negative Indexes
print(thistuple[-4:-2])

print("=== Change Tuple Values ===")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("=== Loop Through a tuple ===")
for x in thistuple:
    print(x)

print("=== Check if Item Exists ===")
if "apple" in thistuple:
    print("I have an apple")

print(len(thistuple))

#  !Once a tuple is created, YOU cannot add items to it.

print("=== Create Tuple with One item ===")
realTuple = ("apple", )
fakeTuple = ("apple")

print(type(realTuple))  # Tuple
print(type(fakeTuple))  # String

print("=== Remove Items ===")
# !Tuples are UNCHANGEABLE, so you cannot remove ITEMS from it, but you can delete the tuble completely

del realTuple

print("=== Join Two Tuples ===")
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
