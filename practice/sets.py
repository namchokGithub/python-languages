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

