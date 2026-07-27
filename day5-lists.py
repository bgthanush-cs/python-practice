#Lists of games

games = ["Free fire", "BGMI", "Clash of clans" , "Mini militia" , "Hill climber"]

print(games[0])
print(games[4])

games[2] = "Temple run"

print(games)
print(len(games))


#Lists of languages

languages = ["Python", "Java" , "C"]

languages.append("JavaScript")
print(languages)

#For Loop
for game in games:
    print(game)

for language in languages:
    print(language)

print("MY Games")
for game in games:
    print("-", game)

print()

print("Programming Languages")
for language in languages:
    print("-", language)

