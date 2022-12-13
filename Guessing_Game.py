secret_number = 19
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Wow you guessed my number!")
        break
else:
    print("You suck")
