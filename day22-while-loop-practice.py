# Day 22 - While Loop Practice
# Input validation

number = int(input("Enter a number: "))

while number <1 or number >10:
    print("Invalid number")
    number = int(input("Enter a number: "))

print("Accepted")    
