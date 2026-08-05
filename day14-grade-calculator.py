# Day 14 - Grade Calculator
# Name: Thanush.B.G

marks = int(input("Enter your marks: "))

if marks > 100:
    print("Invalid marks!")

elif marks <=-1:
    print("Invalid marks!")

elif marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >=50:
    print("Grade: C")

else:
    print("Fail")


