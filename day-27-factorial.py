num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid number!")

else:
    factorial = 1

    for num in range(num, 0, -1):
        factorial *= num
    
    print(factorial)
