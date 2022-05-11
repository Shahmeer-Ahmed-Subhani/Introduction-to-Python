
print("This language is called geez")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:")))


def translate(phrase):
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translate = translate + "g"
        else:
            translate = translate + letter
        
        
        


