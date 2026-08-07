# Day 16 - Nested if
# Name: Thanush.B.G

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")

elif age >= 18:

    has_id = input("Do you have an ID? (yes/no): ").lower()

    if has_id == "yes":
        print("Entry allowed") 

    elif has_id == "no":
        print("Bring your ID")    

    else:
        print("Invalid choice!")

else:
    print("You are underage")

