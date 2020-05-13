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

print("=== Check if Item Exists ===")
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print("=== List Length ===")
print(len(thislist))

print("=== Add items ===")
thislist.append("orange")
print(thislist)

thislist.insert(1, "mango")
print(thislist)

print("=== Remove Items ===")
thislist.remove('mango')
print(thislist)
thislist.pop()
print(thislist)
del thislist[0]
print(thislist)
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("=== Copy list ===")
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

mylist.clear()
mylist = list(thislist)
print(mylist)


