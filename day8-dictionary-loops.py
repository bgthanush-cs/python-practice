# Dictionary Loops

# Creating a dictionary
student = {
    "name" : "Thanush",
    "age" : "17",
    "colege" : "ABC College",
    "branch" : "CSE"
}

# Printing all keys
print("Keys:")
for key in student:
    print(key)

print()

# Printing all values
print("Values:")
for key in student:
    print(student[key])

print()

# Printing keys and values together
print("Key : Value")
for key in student:
    print(key, ":" , student[key])

# Another dictionary
phone = {
    "brand": "Motorola",
    "model": "Moto G86",
    "color": "Blue"
}

print()

# Printing phone details
for key in phone:
    print(key, ":", phone[key])
