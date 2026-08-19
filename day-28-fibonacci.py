n = int(input("Enter the number: "))

first = 0
second = 1


for next in range(0 , n):
    print(first)

    next = first + second
    
    first = second
    second = next
    
    print(next)


   