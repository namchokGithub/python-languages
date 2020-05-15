# Python Dictionaries
# https://www.w3schools.com/python/python_dictionaries.asp

# Example

thisdict = {
    "brand": "Ford"
    ,"model": "Mustang"
    ,"year": 1964
}

print(thisdict)

print("=== Accessing Items ===")

x = thisdict["model"]
print(x)
x = thisdict.get("brand")
print(x)

print("=== Change Values ===")

print(thisdict.get("year"))
thisdict["year"] = 1999
print(thisdict.get("year"))

print("=== Loop Through a Dictionary ===")

for x in thisdict:
    print(x) # print keys

for x in thisdict:
    print(thisdict[x]) # print values

for x in thisdict.values():
    print(x) # print values

for x, y in thisdict.items():
    print(x, y) # print keys and values

print("=== Check if Key Exists ===")

if "mhee" in thisdict: 
    print("Yesss - 1")

if "model" in thisdict: 
    print("Yesss - 2")

print("=== Dictionary Length ===")
print(len(thisdict))

print("=== Adding Items ===")

thisdict["color"] = "red"
print(thisdict)

print("=== Removing Items ===")
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["year"]
print(thisdict)

# or method => dict.clear()

print("=== Copy a Dictionary ===")

thisdict = {
    "brand": "Ford"
    ,"model": "Mustang"
    ,"year": 1964
}

mydict = thisdict.copy()
# or 
mydict = dict(thisdict)

print("=== Nasted Dictionary ===")

myfamily = {
    "child1": {
        "name": "Emil"
        ,"year": 2004
    },
    "child2": {
        "name": "Tobies"
        ,"year": 2007
    },
    "child3": {
        "name": "Linus"
        ,"year": 2011
    }
}

print(myfamily)

# or

child1 = {
    "name" : "a",
    "year" : 1
}
child2 = {
    "name" : "b",
    "year" : 2
}
child3 = {
    "name" : "c",
    "year" : 3
}

myfamily2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily2)