print("MINIGAME!!!")
print("A sect is of 8 giraffes and  there a total of 32 in the jungle")
actual_answer = 4
answer_guessed = ""
answer_count = 0
answer_limit = 5
out_of_guesses = False


while answer_guessed != actual_answer and not(out_of_guesses):
    if answer_count < answer_limit:
        answer_guessed = input("Enter the amount of sects in the jungle")
        answer_count = answer_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You have lost the minigame")
else:
    print("Good game. You have beaten the program")

