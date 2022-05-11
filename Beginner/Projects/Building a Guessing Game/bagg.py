


def sayhi():
    print("Hello user! Your userame will be taken in the further program ")
sayhi()


answer = input("Do you want to play the game? Enter yes or no: ")
if answer == "yes":
        print("Let's begin")
else:
    answer == "no"
    print("Okay, later")
    



abc = input("Do you want to enter a username before playing the game? Enter yes or no: ")
if abc == "yes":
    user = input("Enter username: ")
    print("Hello " + user)
    print("Thank you for entering your user")
else:
    abc == "no"
    print("Let's play the game!")

cont = input("Do you want to proceed playing? ")
if cont == "yes":
    print("Let's continue")
else:
    cont == "no"
    print("Thankyou for Playing")




hc = ""
hclc = 0
hcll = 10000000000000000
hcl = "yellow"
out_of_guesses = False
print("Hint: Yellow")

while hc != hcl and not(out_of_guesses):
    if hclc < hcll:
        hc = input("Enter hair color: ")
        hclc = hclc + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You really failed with that many tries...")
else:
    cont = input("Proceed? ")


    

age = input("Please enter your age.. ")
conf = input("Confirm age.. ")
if age >= str(7):
    print("You are above seven")
    print("Thankyou for entering your age. You can Play this game")
else:
    age < str(7)
    print("You are not eligible to be playing this game")

cont = input("Proceed?")
if cont == "yes":
    print("..")
    print("...")
    print("....")
    print("Proceeding!")
else:
    cont == "no"
    print("Thankyou for playing!")




print("Pick from animal, place, name or thing")
hidden = "animal"
guess = ""
hidden_count = 0
guess_lim = 2
out_of_guesses = False

while guess != hidden and not(out_of_guesses):
    if hidden_count < guess_lim:
        guess = input("Enter guess: ")
        hidden_count = hidden_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You have lost.. Try again")
else:
    cont = input("Continue playing?")

if cont == "yes":
    print("As you wish")
else:
    cont == "no"
    print("Thankyou for playing")




secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Guess the animal: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose..")
else:
    cont = input("Proceed?")

if cont == "yes":
    print("The final step is right ahead you...")
else:
    cont == "no"
    print("Thankyou for playing!")




occassion = "The giraffe is in the park eating grass"
print(occassion)
secret_adjective = "Hungry"
adjective = ""
adjective_guessed = 0
adjective_guess_limit = 5
out_of_guesses = False

while adjective != secret_adjective and not(out_of_guesses):
    if adjective_guessed < adjective_guess_limit:
        adjective = input("Enter the adjective you think is for the giraffe from the given occasion")
        adjective_guessed = adjective_guessed + 1
    else: 
        out_of_guesses = True

if out_of_guesses:
    print("You have lost..")
else:
    print("You have won this game... wellplayed")




print("MINIGAME!!!")
print("A sect is of 8 giraffes and  there a total of 32 in the jungle")
actual_answer = 4
answer_guessed = ""
answer_count = 0
answer_limit = 1
out_of_guesses = False

while answer_guessed != actual_answer and not(out_of_guesses):
    if answer_count < answer_limit:
        answer_guessed = input("Enter the amount of sects in the jungle")
        answer_count = answer_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You have lost the minigame...")
else:
    print("Good game. You have beaten the program")




print(input("Please run the program to play this game again"))
print("Thankyou for playing")
print("This program is my first program. Made on second of January, 2022")

print("MINIGAME!!")
def translate(phrase):
    translation = ""
    for letter in(phrase):
        if letter.lower in "aeiou":
            translation = translation + "g"
            print(translation).count("g")
            if letter.isupper():
                translation = translation + "G"
        else:
            translation = translation + letter
    return(translation)

print(translate(input("Enter a phrase: ")))

    

            
