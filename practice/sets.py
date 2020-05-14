# Python Sets
# https://www.w3schools.com/python/python_sets.asp

# Example
thisset = {"apple", "banana", "cherry"}
print(thisset)

print("=== Access items ===")
# *You cannnot access items in a set by referring to an index.

for x in thisset:
    print(x)

# Check if "items" in present in the set
print("banana" in thisset) # True
print("mango" in thisset) # False

# once a set is created, you cannot change its items, but you can add new items.
print("=== Add items ===")

thisset.add("orange")
print(thisset)

# Update sets
# add multi items
set1 = {"apple", "mango", "banana"}
set1.update(["a", "b", "c"])
print(set1)

print("=== Remove items ===")
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("cherry")
print(thisset)

print(set1)
set1.pop()
print(set1)
set1.clear()

del set1
