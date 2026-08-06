# Day-15 - Logical Operators.py
# Name: Thanush.B.G

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no):")

if age >= 18 and has_id == "yes":
    print("Entry Allowed")

elif age >= 18 and has_id == "no":
    print("Bring your ID")

elif age <= 0:
    print("Invalid age!")

else:
    print("You are underage")