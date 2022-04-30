camelCase = input("camelCase: ")

print("snake_case: ", end="")

# Loop through letters
for letter in camelCase:
    if letter.isupper():
        # Underscore and lowercase
        print("_" + letter.lower(), end="")

    else:
        print(letter, end="")     

      