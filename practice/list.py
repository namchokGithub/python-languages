# Python Lists
# https://www.w3schools.com/python/python_lists.asp

# Example
thislist = ["apple", "banana", "cherry"]

# Print lists
print(thislist)

print("=== Access Item ===")
print(thislist[1])

# Nagative indexing
print(thislist[-1])

# Range of Indexes
thislist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

print("=== Range of Nagative Indexes ===")
print(thislist[-4:-1])

print("=== Change Item Value ===")

thislist[1] = "blackcurrent"
print(thislist)

print("=== Loop Through a List ===")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)