# Day 12 - Error Handling
# Name: Thanush.B.G

try:
    age = int(input("Enter your age: "))

    print("Your age is:", age)

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")       

except ValueError:
    print("Invalid input! Please enter a number.")

if age < 0:
    print("Age cannot be negative.")               

      