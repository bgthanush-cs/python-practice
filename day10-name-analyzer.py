# Day 10 - Name Analyzer
# Name: Thanush.B.G

name = input("Enter your name: ")

print("\n----- Name Analysis -----")
print("Original Name:", name)
print("Length       :", len(name))
print("Uppercase    :", name.upper())
print("Lowercase    :", name.lower())
print("First Letter :", name[0])
print("Last Letter  :", name[-1])

letter =input("\nEnter a letter to search: ")

if letter in name:
    print("✅ Letter found!")
else:
    print("❌ Letter not found!")    