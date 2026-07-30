# Dictionary Loops

student = {
    "name" : "Thanush",
    "age" : "17",
    "colege" : "ABC College",
    "branch" : "CSE"
}

print("Keys:")
for key in student:
    print(key)

print()

print("Values:")
for key in student:
    print(student[key])

print()

print("Key : Value")
for key in student:
    print(key, ":" , student[key])
