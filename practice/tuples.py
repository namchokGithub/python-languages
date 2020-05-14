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

