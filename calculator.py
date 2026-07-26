# Mini Project 1 - Calculator

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a , b):
    return a * b

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("Sum:", add(num1, num2))
print("Differance:", substract(num1, num2))
print("Product:", multiply(num1, num2))
