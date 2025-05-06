python = "Python is Amazing"
print(python.upper())
print(python.lower())
print(python[0].islower())
print(len(python))
print(python.replace("Python", "C++"))

index = python.index("i")
print(index)
index = python.index("i", index + 1)
print(index)

print(python.find("Java")) # return -1
# print(python.index("Java")) # error

print(python.count("n"))

