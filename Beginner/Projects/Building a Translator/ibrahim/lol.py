
hidden = "Hello World"
g = ""
h_c = 0
g_l = 100
out_of_guesses = False

while g != hidden and not(out_of_guesses):
    if h_c < g_l:
        g = input("Enter guess: ")
        h_c = h_c + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("SHTUPID")
else:
    print("ok good")
