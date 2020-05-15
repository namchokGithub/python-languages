# Python While Loops
# https://www.w3schools.com/python/python_while_loops.asp

print("=== The while Loop ===")
i = 3
while i < 6:
    print(i)
    i+=1

print("=== The break Statement ===")
i = 1
while i < 5:
    print(i)
    if i==3:
        break
    i+=1

print("=== The continue Statement ===")
i=0
while i < 6:
    i += 1
    if i==3:
        continue
    print(i)

print("=== The else Statemet ===")
i = 1 
while i < 6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

