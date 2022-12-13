import random

charm = True

choice = ["Yes", "No"]

while charm is True:
    question = input(" Ask a Yes/No question: ")
    print(random.choice(choice))
