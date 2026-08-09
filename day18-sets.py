#Day 18 - Sets 
#Name: Thanush B G

# Creating a set
games = {"Minecraft","BGMI","Free Fire","Minecraft"}

print(games)

#Adding an item
games.add("GTA")

print(games)

#Checking the number of unique items 
print(len(games))


#Converting a list into a set
students = [
    "Thanush",
    "Arjun",
    "Rahul",
    "Thanush",
    "Meera",
    "Arjun",
    "Vishnu"
]

unique_students =set(students)

print(unique_students)
print(len(unique_students))
