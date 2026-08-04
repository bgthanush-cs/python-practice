# Day 13 - Modules
# Name: Thanush.B.G

import random

print("Lucky Number Generator")

number = random.randint(1,100)

print("Your lucky number is:", number)

print()

import random

print("Movie Picker")

movies = [
    "Interstellar",
    "Avengers",
    "KGF",
    "Your Name"
]

print(random.choices(movies))