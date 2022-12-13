secret_word = "Poop"
guess_tries = 0
guess_limit = 6
print("I will give you a hint. This is something you do everyday.")
while guess_tries < guess_limit:
    guess = input("Try to guess my secret word: _ _ _ _").capitalize()
    guess_tries += 1
    if guess == secret_word:
        print("Wow! Congratulations you figured out my word!")
        break
    else:
        print("No, that isn't my word, try again... ")
if guess_tries == guess_limit:
    print("You really suck at Hangman...")
