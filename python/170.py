text = input("Enter a string: ")
frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("Character frequency:")

for character, count in frequency.items():
    print(character, ":", count)